#!/usr/bin/env python3
"""
Hatena Blog publisher via AtomPub API.
Reads markdown files from posts/ directory and publishes/updates them.
"""

import os
import re
import sys
import base64
from pathlib import Path
from datetime import datetime
from xml.sax.saxutils import escape

import requests
from xml.etree import ElementTree as ET

# ── Config from environment variables ──────────────────────────────────────
HATENA_ID = os.environ["HATENA_ID"]
HATENA_API_KEY = os.environ["HATENA_API_KEY"]
BLOG_DOMAIN = os.environ["BLOG_DOMAIN"]

BASE_URL = f"https://blog.hatena.ne.jp/{HATENA_ID}/{BLOG_DOMAIN}/atom/entry"

NAMESPACES = {
    "atom": "http://www.w3.org/2005/Atom",
    "app": "http://www.w3.org/2007/app",
}


def auth_header() -> dict:
    token = base64.b64encode(f"{HATENA_ID}:{HATENA_API_KEY}".encode()).decode()
    return {"Authorization": f"Basic {token}"}


# ── Frontmatter helpers ─────────────────────────────────────────────────────

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def parse_frontmatter(text: str) -> tuple[dict, str]:
    """Return (frontmatter_dict, body)."""
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}, text
    fm = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            key, _, val = line.partition(":")
            fm[key.strip()] = val.strip().strip('"')
    body = text[m.end():]
    return fm, body


def write_entry_id(md_path: Path, entry_id: str) -> None:
    """Write hatena_entry_id back into the markdown file."""
    text = md_path.read_text(encoding="utf-8")
    updated = re.sub(
        r'(hatena_entry_id:\s*)"?"?.*?"?',
        f'hatena_entry_id: "{entry_id}"',
        text,
    )
    md_path.write_text(updated, encoding="utf-8")


# ── AtomPub helpers ─────────────────────────────────────────────────────────

def build_entry_xml(title: str, body: str) -> str:
    # Split any "]]>" in body across two adjacent CDATA sections so it cannot
    # prematurely terminate the outer CDATA block:  ]]> → ]] + ><![CDATA[
    safe_body = body.replace("]]>", "]]]]><![CDATA[>")
    return f"""<?xml version="1.0" encoding="utf-8"?>
<entry xmlns="http://www.w3.org/2005/Atom"
       xmlns:app="http://www.w3.org/2007/app">
  <title>{escape(title)}</title>
  <content type="text/plain"><![CDATA[{safe_body}]]></content>
  <app:control>
    <app:draft>no</app:draft>
  </app:control>
</entry>"""


def post_entry(title: str, body: str) -> str:
    """POST new entry, return entry_id."""
    xml = build_entry_xml(title, body)
    headers = {**auth_header(), "Content-Type": "application/atom+xml"}
    resp = requests.post(BASE_URL, data=xml.encode("utf-8"), headers=headers)
    resp.raise_for_status()
    root = ET.fromstring(resp.text)
    entry_id_el = root.find("atom:id", NAMESPACES)
    if entry_id_el is None:
        raise ValueError("entry id not found in response")
    # id text looks like: tag:blog.hatena.ne.jp,...:entry/26006613388827581
    return entry_id_el.text.split("/")[-1]


def put_entry(entry_id: str, title: str, body: str) -> None:
    """PUT (update) existing entry."""
    xml = build_entry_xml(title, body)
    headers = {**auth_header(), "Content-Type": "application/atom+xml"}
    url = f"{BASE_URL}/{entry_id}"
    resp = requests.put(url, data=xml.encode("utf-8"), headers=headers)
    resp.raise_for_status()


# ── Main ────────────────────────────────────────────────────────────────────

def process_file(md_path: Path) -> None:
    text = md_path.read_text(encoding="utf-8")
    fm, body = parse_frontmatter(text)

    title = fm.get("title", md_path.stem)
    entry_id = fm.get("hatena_entry_id", "").strip()

    if entry_id:
        print(f"[UPDATE] {md_path.name} → entry/{entry_id}")
        put_entry(entry_id, title, body.strip())
    else:
        print(f"[CREATE] {md_path.name}")
        new_id = post_entry(title, body.strip())
        print(f"  → created entry/{new_id}")
        write_entry_id(md_path, new_id)


def main() -> None:
    posts_dir = Path("posts")
    if not posts_dir.exists():
        print("posts/ directory not found", file=sys.stderr)
        sys.exit(1)

    md_files = sorted(posts_dir.glob("*.md"))
    if not md_files:
        print("No markdown files found in posts/")
        return

    for md_path in md_files:
        process_file(md_path)


if __name__ == "__main__":
    main()

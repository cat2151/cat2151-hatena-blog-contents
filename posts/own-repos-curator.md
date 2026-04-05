---
title: "（随時更新）GitHubの自分の公開リポジトリ一覧を自動生成させてみる"
hatena_entry_id: "tag:blog.hatena.ne.jp,2013:blog-cat2151-6435988827677137845-17179246901373353453"
---

## 目次

- [github](#group-github) (11件)
- [ym2151](#group-ym2151) (9件)
- [tonejs](#group-tonejs) (6件)
- [obsidian](#group-obsidian) (5件)
- [webaudio](#group-webaudio) (5件)
- [mml](#group-mml) (4件)
- [blog](#group-blog) (3件)
- [zundamon](#group-zundamon) (3件)
- [chromeextension](#group-chromeextension) (2件)
- [daw](#group-daw) (2件)
- [fightinggame](#group-fightinggame) (1件)
- [vibes](#group-vibes) (1件)
- [etc](#group-etc) (11件)
- [stub](#group-stub) (18件)

## 概要

cat2151のGitHubリポジトリをグループ別に一覧化したものです。

最終更新: 2026-04-05

<a id="group-github"></a>

## github

### [own-repos-curator-to-hatena](https://cat2151.github.io/own-repos-curator-to-hatena/README.ja.html)

紹介文を、はてなブログに投稿

- linkの選択もここで行っています。JekyllのREADME.ja.htmlを選ぶ処理はここ。

タグ: `blog`

### [own-repos-curator](https://cat2151.github.io/own-repos-curator/README.ja.html)

リポジトリ一覧を軸に、紹介文のメンテを効率化

- どんなとき嬉しいか：リポジトリ一覧を紹介したいが紹介文のメンテが面倒なとき
- 先行事例：見つからなかった

タグ: `tui`

### [own-repos-curator-data](https://cat2151.github.io/own-repos-curator-data/)

リポジトリ群を訪問者にわかりやすく可視化

- どんなとき嬉しいか：インタラクティブにリポジトリ群をフィルタして紹介したいとき

タグ: `browser`

### [cat-self-update](https://cat2151.github.io/cat-self-update/README.ja.html)

self update機能を実現するライブラリ

- どんなとき嬉しいか：Rustでセルフアップデートを自作するのが面倒なとき
- 先行事例：オーバースペックなものしか見つからなかった


タグ: `vibes`

### [cat-gh-repo-creator](https://cat2151.github.io/cat-gh-repo-creator/README.ja.html)

localリポジトリをGitHubに登録

タグ: `github` `tui` `vibes`

### [norenwake](https://cat2151.github.io/norenwake/README.ja.html)

リポジトリを新リポジトリに履歴を維持して暖簾分け

タグ: `github` `tui` `vibes`

### [cat-repo-auditor](https://cat2151.github.io/cat-repo-auditor/README.ja.html)

全リポジトリの状況を可視化して管理

タグ: `github` `tui`

### [cat-github-watcher](https://cat2151.github.io/cat-github-watcher/README.ja.html)

GitHub Copilot Coding Agentを自動化して、人間の作業をissue作成とPRレビューだけにして楽をする

タグ: `cui`

### [cat-jekyll-config-generator](https://cat2151.github.io/cat-jekyll-config-generator/)

（説明なし）

タグ: `cui`

### [github-actions](https://cat2151.github.io/github-actions/README.ja.html)

CI。再利用可能ワークフロー

タグ: `github`

### [cat2151.github.io](https://cat2151.github.io/)

リポジトリ一覧（自動生成）

タグ: `browser`

<a id="group-ym2151"></a>

## ym2151

### [sixel-playground](https://github.com/cat2151/sixel-playground/blob/HEAD/README.ja.md)

FM音源波形をTUIでグラフ表示するためのライブラリ

タグ: `audio` `tui`

### [web-ym2151](https://cat2151.github.io/web-ym2151/)

FM音源をブラウザで鳴らすためのライブラリ

タグ: `audio` `browser`

### [ym2151-log-editor](https://cat2151.github.io/ym2151-log-editor/README.ja.html)

FM音源レジスタ書き込みログを編集するTUI

タグ: `audio` `tui`

### [ym2151-log-play-server](https://cat2151.github.io/ym2151-log-play-server/README.ja.html)

FM音源を鳴らすためのライブラリ

タグ: `audio`

### [cat-edit-mml](https://cat2151.github.io/cat-edit-mml/)

MMLエディタ

タグ: `audio` `mml` `tui`

### [ym2151-tone-editor](https://cat2151.github.io/ym2151-tone-editor/README.ja.html)

FM音源音色エディタ

タグ: `audio` `tui`

### [smf-to-ym2151log-rust](https://cat2151.github.io/smf-to-ym2151log-rust/)

スタンダードMIDIファイルをFM音源で鳴らすためのライブラリ

タグ: `audio` `browser`

### [mmlabc-to-smf-rust](https://cat2151.github.io/mmlabc-to-smf-rust/)

FM音源MMLコンパイラ

タグ: `audio` `compiler`

### [cat-play-mml](https://cat2151.github.io/cat-play-mml/README.ja.html)

コマンドライン引数にcdeを書くだけでドレミが鳴るFM音源MMLプレイヤー

タグ: `audio` `cui`

<a id="group-tonejs"></a>

## tonejs

### [tonejs-step-sequencer](https://cat2151.github.io/tonejs-step-sequencer/)

Tone.jsのステップシーケンサ。ランダム音色機能つき

タグ: `audio` `browser`

### [cat-oscilloscope](https://cat2151.github.io/cat-oscilloscope/)

micやWAVファイルの音を可視化。位相を揃えて波形を見やすく表示

- 実際は位相を揃える処理に課題があり、micの音の位相は揃ったり揃わなかったりです

タグ: `audio` `browser`

### [cat-oscillator-sync](https://cat2151.github.io/cat-oscillator-sync/)

オシレータシンク音色で遊ぼう

タグ: `audio` `browser`

### [tonejs-mml-to-json](https://cat2151.github.io/tonejs-mml-to-json/)

Tone.js用MMLコンパイラ。ランダム音色demoつき

- ランダム音色demoは画面左下のtone edit & effect edit demo をクリック

タグ: `audio` `browser` `compiler`

### [tonejs-json-sequencer](https://cat2151.github.io/tonejs-json-sequencer/)

Tone.jsをデータで演奏。面倒なプログラミングは不要

タグ: `audio` `browser`

### [postmate-midi-experimental](https://cat2151.github.io/postmate-midi-experimental/)

（説明なし）

タグ: `audio` `browser`

<a id="group-obsidian"></a>

## obsidian

### [obsidian-cat-jump](https://cat2151.github.io/obsidian-cat-jump/README.ja.html)

a-zキーのラベルを表示して行ジャンプ。直感的で素早い

タグ: `obsidian`

### [quartz-transformer-mmlabc](https://cat2151.github.io/quartz-transformer-mmlabc/README.ja.html)

Obsidianで書いたMMLとコード進行を、デジタルガーデン上でクリックして五線譜表示と演奏できるようにする

タグ: `audio` `blog` `browser`

### [obsidian-plugin-mmlabc](https://cat2151.github.io/obsidian-plugin-mmlabc/)

ObsidianでMMLとコード進行を書いて五線譜表示と演奏をする

タグ: `audio`

### [cat-obsidian-templater-scripts](https://cat2151.github.io/cat-obsidian-templater-scripts/README.ja.html)

Obsidian用Templaterスクリプト集

### [recursive-folding](https://cat2151.github.io/recursive-folding/)

Obsidianの折りたたみを再帰的に行う

<a id="group-webaudio"></a>

## webaudio

### [easychord2mml](https://cat2151.github.io/easychord2mml/)

（説明なし）

タグ: `audio` `browser`

### [chord2mml](https://cat2151.github.io/chord2mml/README.ja.html)

コード進行をMMLに変換

タグ: `audio` `browser` `compiler`

### [easymmlabc](https://cat2151.github.io/easymmlabc/)

（説明なし）

タグ: `audio` `browser`

### [mml2abc](https://cat2151.github.io/mml2abc/README.ja.html)

MMLをabc notationにトランスパイル

タグ: `audio` `browser` `transpiler`

### [easyabcjs6](https://cat2151.github.io/easyabcjs6/)

（説明なし）

タグ: `audio` `browser`

<a id="group-mml"></a>

## mml

### [mml-repl-like](https://cat2151.github.io/mml-repl-like/README.ja.html)

（説明なし）

タグ: `audio` `browser`

### [mml-template-generator](https://cat2151.github.io/mml-template-generator/)

MMLをほかのMMLに変換

タグ: `audio` `browser` `transpiler`

### [MML-editor](https://cat2151.github.io/MML-editor/)

（説明なし）

タグ: `audio` `browser`

### [MML-quick-player](https://cat2151.github.io/MML-quick-player/)

（説明なし）

タグ: `audio` `browser`

<a id="group-blog"></a>

## blog

### [cat2151-hatena-blog-contents](https://cat2151.github.io/cat2151-hatena-blog-contents/)

はてなブログの投稿記事をGitHubで書く

タグ: `blog`

### [digital-garden](https://cat2151.github.io/digital-garden/)

ブログとwikiが合体したスタイル。書きかけ記事をガーデニングして育てていく

タグ: `blog` `browser`

### [cat2151-zenn-contents](https://cat2151.github.io/cat2151-zenn-contents/)

Zenn投稿記事をGitHubで書く

タグ: `blog`

<a id="group-zundamon"></a>

## zundamon

### [mascot-render-server](https://cat2151.github.io/mascot-render-server/README.ja.html)

ずんだもん等のデスクトップマスコット

タグ: `psd` `zundamon`

### [voicevox-playground-tui](https://cat2151.github.io/voicevox-playground-tui/README.ja.html)

ずんだもん等をしゃべらせ、デスクトップマスコットも表示

タグ: `audio` `tui` `zundamon`

### [voicevox-playground](https://cat2151.github.io/voicevox-playground/)

ずんだもん等をしゃべらせる（ブラウザ）

タグ: `audio` `browser`

<a id="group-chromeextension"></a>

## chromeextension

### [bluesky-text-to-audio](https://cat2151.github.io/bluesky-text-to-audio/README.ja.html)

BlueskyにMML演奏/DAW演奏/ずんだもん読み上げ ボタンをつける

タグ: `audio` `browser` `zundamon`

### [zenn-qiita-mute-warning](https://cat2151.github.io/zenn-qiita-mute-warning/README.ja.html)

ZennとQiitaでmuteしたuserのBluesky投稿や記事本体に警告を出す

タグ: `browser`

<a id="group-daw"></a>

## daw

### [clap-mml-play-server](https://cat2151.github.io/clap-mml-play-server/README.ja.html)

Surge XTの音色をオフラインレンダリングするためのライブラリ

タグ: `audio` `daw` `mml`

### [clap-mml-render-tui](https://cat2151.github.io/clap-mml-render-tui/README.ja.html)

MMLのDAW

タグ: `audio` `daw` `tui`

<a id="group-fightinggame"></a>

## fightinggame

### [fighting-game-button-challenge](https://cat2151.github.io/fighting-game-button-challenge/README.ja.html)

格ゲー（スト6）のレバーレスコントローラー用ボタン練習アプリ

<a id="group-vibes"></a>

## vibes

### [claude-chat-code](https://cat2151.github.io/claude-chat-code/README.ja.html)

ClaudeChat自動化

タグ: `tui` `vibes`

<a id="group-etc"></a>

## etc

### [cat-window-watcher](https://cat2151.github.io/cat-window-watcher/README.ja.html)

（説明なし）

### [cat-clipboard-launcher](https://cat2151.github.io/cat-clipboard-launcher/)

（説明なし）

タグ: `tui`

### [cat-file-watcher](https://cat2151.github.io/cat-file-watcher/README.ja.html)

ファイル監視 / プロセス監視。小規模TOMLを書くだけで楽にメンテをしたい用途向け

タグ: `cui`

### [mini-command-palette-mery](https://cat2151.github.io/mini-command-palette-mery/)

（説明なし）

### [mini-command-palette-sakura-editor](https://cat2151.github.io/mini-command-palette-sakura-editor/)

（説明なし）

### [mini-command-palette-hidemaru](https://cat2151.github.io/mini-command-palette-hidemaru/README.ja.html)

（説明なし）

### [migemo-auto-install-for-windows](https://cat2151.github.io/migemo-auto-install-for-windows/)

（説明なし）

### [migemo-auto-install-for-windows-and-python](https://cat2151.github.io/migemo-auto-install-for-windows-and-python/)

（説明なし）

### [wsl2-docker-mingw-hello](https://cat2151.github.io/wsl2-docker-mingw-hello/)

（説明なし）

### [cygwin-auto-get-install](https://cat2151.github.io/cygwin-auto-get-install/)

（説明なし）

### [msys2-auto-install](https://cat2151.github.io/msys2-auto-install/README.ja.html)

（説明なし）

<a id="group-stub"></a>

## stub

### [cross-origin-hub](https://cat2151.github.io/cross-origin-hub/)

（説明なし）

タグ: `audio` `browser`

### [postmate-midi](https://github.com/cat2151/postmate-midi)

こちらは未着手。本体は https://cat2151.github.io/postmate-midi-experimental/ 側にある

タグ: `audio` `browser`

### [lib-installation-examples](https://github.com/cat2151/lib-installation-examples)

（説明なし）

### [tonejs-tone-editor](https://github.com/cat2151/tonejs-tone-editor)

まだ音色エディタを作っていない。代わりに別リポジトリでランダム音色demoがある

- 別リポジトリのランダム音色demoとは : https://cat2151.github.io/tonejs-mml-to-json/tone-edit-demo/

タグ: `audio` `browser`

### [tonejs-mml-to-json-pest](https://github.com/cat2151/tonejs-mml-to-json-pest)

（説明なし）

### [chord2mml-pest](https://github.com/cat2151/chord2mml-pest)

（説明なし）

### [tree-sitter-wasm-c-use-example](https://github.com/cat2151/tree-sitter-wasm-c-use-example)

（説明なし）

### [tree-sitter-wasm-c-generate-example](https://github.com/cat2151/tree-sitter-wasm-c-generate-example)

（説明なし）

### [tree-sitter-wasm-rust-example](https://github.com/cat2151/tree-sitter-wasm-rust-example)

（説明なし）

### [chord2mml-rust](https://cat2151.github.io/chord2mml-rust/)

（説明なし）

### [wavlpf](https://cat2151.github.io/wavlpf/)

（説明なし）

タグ: `audio` `browser`

### [super-easy-vim](https://cat2151.github.io/super-easy-vim/)

vimに過剰なヘルプ説明をつけたジョークアプリを目指しているが着手直後で停滞している

タグ: `tui`

### [cat-incremental-search-filter](https://cat2151.github.io/cat-incremental-search-filter/)

（説明なし）

### [display-image-1sec](https://github.com/cat2151/display-image-1sec/blob/HEAD/README.ja.md)

（説明なし）

### [cat-active-window-logger](https://github.com/cat2151/cat-active-window-logger/blob/HEAD/README.ja.md)

（説明なし）

### [easy-web-midi-synth-template](https://cat2151.github.io/easy-web-midi-synth-template/)

（説明なし）

タグ: `audio` `browser`

### [easy-web-midi-sequencer-template](https://cat2151.github.io/easy-web-midi-sequencer-template/)

（説明なし）

タグ: `audio` `browser`

### [games-crisp-game-lib](https://cat2151.github.io/games-crisp-game-lib/)

（説明なし）


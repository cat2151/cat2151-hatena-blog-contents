# cat2151-hatena-blog-contents

## 概要

localでpostsを書いてGitHubにcommit pushするだけで、
はてなブログに、投稿 or 更新 するシステム

Claudeに作らせた

## 使い方

### 準備

#### 設定
- 以下をGitHubのリポジトリのsecretsに設定する：
  - HATENA_API_KEY
  - HATENA_ID
  - BLOG_DOMAIN

#### 配置
- 以下を配置する：
  - GitHub workflow ymlファイル
  - scripts/ 配下のscriptファイル

### 投稿（新規）
- posts/ 配下に、新しく、投稿したい記事をmarkdownで書く
- はてなブログを開き、投稿されていることを確認する

### 投稿（更新）
- posts/ 配下のmarkdownを修正する
- はてなブログを開き、修正が反映されていることを確認する

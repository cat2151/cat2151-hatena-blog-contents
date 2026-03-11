---
title: "GitHubから、はてなブログに投稿する"
hatena_entry_id: "tag:blog.hatena.ne.jp,2013:blog-cat2151-6435988827677137845-17179246901363848497"
---

## 3行で説明
- はてなブログにGitHubから投稿できたら面白そう
- 調査しつつ、Claudeと壁打ちした
- できた。やったぜ！Claude便利だね

## 詳細

## モチベ、なぜGitHub？
- Zennと同様の執筆体験になるのはメリット。認知負荷を下げられる
    - 執筆時の認知負荷は基本的に低いほどよい。言い換えると、ユーストレスを最大化し、ディストレスを最小化するほうがよく、ディストレスになりうるタイプの認知負荷は最小化するほうがよい
- GitHubで統合的に版管理できるのはメリット
- なんか面白そう、技術的なチャレンジや探索が面白そう

### 実装において発生した課題と対策
- 改行まわりで複数回Claudeがバグっていて時間がかかった
    - 結果的にissueを投げまくっていたら解決したので、期間は長いが工数は小さい
    - 原因は、htmlとして扱われること（とmarkdown指定しても想定した挙動をしないこと）
    - 対策は、先にmarkdownをパースしてhtml化、をすること（もちろん自動で）

### 試してわかった、意外なメリット
- UXがよいと感じた。なぜなら書いてからdeploy（記事への反映）までが爆速
    - おそらく小規模だから。おそらくボトルネックが、当リポジトリのCIのmarkdown to htmlレンダラ、の部分として、そこが小規模で軽量、爆速だから

## リポジトリ
- [cat2151-hatena-blog-contents](https://github.com/cat2151/cat2151-hatena-blog-contents/)

## 参考：リポジトリ README （GitHub Pages）
- [cat2151-hatena-blog-contents](https://cat2151.github.io/cat2151-hatena-blog-contents/)

---
layout: post
title: '断線状態で Jekyll remote theme を使いたかったので'
---

Jekyll:None

ネットワークに接続していない環境で Jekyll remote theme を利用したサイトの保守をする方法を試してみました。

---

Jekyll を使って[担当している講義の静的ウェブサイト](https://wakita.github.io/classes/)を運営しています。このウェブサイトでは 

GitHub は Jekyll は 10 種類程度のテーマを選択することができますが、それに飽き足らない場合には GitHub にホスティングされている[遠隔テーマ(remote theme)](https://jekyllrb.com/docs/themes/)に対応したテーマを利用することもできます。わたしが利用している [basically basic](https://github.com/mmistakes/jekyll-theme-basically-basic) というテーマもそうした遠隔テーマのひとつです。

遠隔テーマの使い方は簡単で、基本的には `Gemfile` をすこし調整した上で、`_config.yml` のなかの普通は `theme: <テーマの名前>` と書くところを `remote_theme: "<テーマの名前>"` に置き換えるだけです。具体的な設定については[遠隔テーマ(remote theme)](https://jekyllrb.com/docs/themes/)の内容や[`basically basic`のReadme](https://github.com/mmistakes/jekyll-theme-basically-basic/blob/master/README.md)を見て下さい。具体的な設定については[私のサイトのリポジトリ](https://github.com/wakita/classes)のなかの `Gemfile` と `_config.yml` が参考になるでしょう。

これでしばらく快適に過していたんですが、ひとつ困ったことを見つけました。移動中、ネットワーク接続を停止しているときに `bundle exec jekyll build ...` すると、サイトの再構築がエラーを生じるのです。原因は `remote_theme:` 設定があると、再構築のたびに GitHub にアクセスするためのようです。`Gemfile` に該当する Gem を追加してもだめでした。

# 悩み

`remote_theme:` 機能は使いたいけれど、断線環境では再構築ができないという悩みです。

# 解決の方針

そこで、Jekyll の環境設定を二種類用意することにしました。

遠隔テーマ設定 (`_config.yml`)
: こちらの設定は GitHub に push するためのものです。すでに書いたように、この設定では断線環境での再構築ができません。

ローカルテーマ設定 (`etc/_config.yml`)
: こちらの設定は手元でビルドするためのものです。`Gemfile` に記載したテーマの Gem を利用して環境を構築し、手元のウェブサーバで内容を確認できます。環境が手元のパソコンに閉じているため、断線環境下で利用できます。

`_config.yml` と `etc/_config.yml` の内容の違いは、前者が `remote_theme:` 設定を用いるのに対し、後者が `theme:` 設定を施す点だけです。以下に私の設定の差分を示します。

~~~ .patch
*** _config.yml	Sat Sep 18 06:10:59 2021
--- etc/_config.yml	Sat Sep 18 06:20:45 2021
***************
*** 67,74 ****
        year: "2022"
  
  # Build settings
! remote_theme: "mmistakes/jekyll-theme-basically-basic"
! #theme: jekyll-theme-basically-basic
  
  plugins:
    - jekyll-feed
--- 67,74 ----
        year: "2022"
  
  # Build settings
! #remote_theme: "mmistakes/jekyll-theme-basically-basic"
! theme: jekyll-theme-basically-basic
  
  plugins:
    - jekyll-feed
~~~

そして以下がサイト再構築に用いているスクリプトです。

~~~ .sh
#!/bin/sh

patch < etc/_config.patch
bundle exec jekyll build --config etc/_config.yml --destination $HOME/Sites/classes --incremental --watch $*
~~~

`patch` に前述の差分を喰わせて、`etc/_config.yml` を生成し、`bundle exec jekyll build` では生成したばかりの `etc/_config.yml` を利用します。

サイトの保守には、`_config.yml` を編集し、手元での再構築のための設定はその都度、自動生成されます。

これで断線環境でも、サイトの保守ができるようになりました。もちろん、サイトを公開するときはネットワークに接続しますけれど。

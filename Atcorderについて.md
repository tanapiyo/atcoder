http://tatamo.81.la/blog/2018/12/07/atcoder-cli-tutorial/

## コンテストの種類

- AtCoder Beginner Contest (通称 ABC、初級者向け)
- AtCoder Regular Contest (通称 ARC、中上級者向け)
- AtCoder Grand Contest (通称 AGC、あらゆる層向けだが最上級者も楽しめる内容)
- ABC の B 問題までは全探索とかでなんとかなる

## 初級

- for で全組み合わせを検索
- C 問題だと計算量を気にしなければいけないかも
- 目安：1s に処理できる for は 10^8
- 後ろから greedy するといいこともあるかも

- DP
  https://qiita.com/drken/items/dc53c683d6de8aeacf5a

## 勉強できるサイト

- atcoder problems
  https://kenkoooo.com/atcoder/#/table/
- atcoder tags
  https://atcoder-tags.herokuapp.com/
- cafecoder
  https://www.cafecoder.top/

##　環境構築
https://qiita.com/Adaachill/items/3d4ddad56c5c2cc372cd

```
pip3 install online-judge-tools
npm install -g atcoder-cli
```

### 初期設定

```
//ログイン
acc login
//ログイン確かめる
acc session
//online-judge-toolsもログイン
oj login https://beta.atcoder.jp/
```

### コンテスト用のディレクトリを作る

```
//コンテストのディレクトリ作る
acc new abc101
//あとは対話式で解く問題を選択する

//テスト
oj t -c " python3 ./a.py" -d ./tests/

//submit
acc submit main.cpp

//次の問題
 acc add
```

## 勉強方法

- 解説読んでやり方を理解する
- 類題をといてみるが、最初は python とかでかく
- 一通りやったらまたやりなおす
- デバッグするのと図示する

- 基本的には問題を見て考察する（5~15 分）
- 解けそうなら実装する、わからなければ解説を見る
- 解説でわかれば実装、わからなければ解説ブログを見る
- 解説ブログでわかれば実装、わからなければコードを見る
- コードを写経しながら理解に努める

- 最初は知識を詰め込むために写経メイン。ただ自分で実装復習しないと知識定着できない
- 「よさげな Web 記事を見る」->「実装する」->「過去問で試す」->「ライブラリにして使いやすくしておく」

## 環境構築

- vscode のスニペットにライブラリをつくる
  - ファイル＞基本設定＞ユーザースニペット
- atcoder unittest を入れる
  - https://qiita.com/YujiSoftware/items/00ce688ce5dde627ec36
- pypy にする
  - https://qiita.com/snjot/items/d7690f38e34277d672a1

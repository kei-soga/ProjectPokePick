# What is ProjectPokePick(P3)

ProjectPokePick(P3)はポケモン対戦において、自分の手持ちの中から最も勝率の良い3体を選出するAIエージェントです。

また、そのAIエージェントの学習モデルを構築するためのプロジェクトも含みます。

## 環境構築

### Windows, Mac, Linux(Desktop版)

[Docker Desktop](https://www.docker.com/ja-jp/products/docker-desktop/)をインストールしてください。

### Linux(Server版)、WSL

[Docker Engine](https://docs.docker.com/engine/install/)をインストールしてください。

必要に応じて、Docker Composeもインストールしてください。

## クイックスタート

### 1. 各サービスを起動する

下記コマンドを実行し、Pokemon ShowdownとP3エージェントを起動する。

`docker compose up -d`

### 2. 相手と自分のチームビルドを選択する

*TODO: 説明追加*

### 3. AIエージェントの実行

*TODO: 説明追加*

projectpokepickフォルダ配下のモジュールを絶対パスでインポートするために下記コマンドを使う。

`python -m projectpokepick.main`

### 4. 出力の確認

*TODO: 説明追加*

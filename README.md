# menstagram-ai

<img src="logo.png" width="500">

**🍜 SUSURU FOREVER, SUSURU ANYWHERE 🍜**  
menstagram-aiはMenstagramのラーメン判定API開発のためのリポジトリです。

### 環境構築

```bash
$ git clone https://github.com/uyupun/menstagram-ai.git
$ cd menstagram-ai
```

### 環境構築(学習)
学習は処理が重いので基本的にはホストマシン側で実行する.

```bash
$ pipenv install --dev           // ライブラリのインストール
$ pipenv run download            // 学習データの自動収集
$ pipenv run separate            // 学習データの分類
$ pipenv run train               // 学習
$ pipenv run test                // 学習結果の検証
```

### 環境構築(Web API)

```bash
$ docker network create menstagram  // menstagram-apiですでに作成している場合は実行しなくて良い
$ make init
```

### コマンド

```bash
$ make up       // 起動(localhost:8001)
$ make down     // 終了
$ make sh       // Bashの起動
```
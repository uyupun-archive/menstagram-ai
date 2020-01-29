# menstagram-ai

<img src="logo.png" width="500">

**🍜 SUSURU FOREVER, SUSURU ANYWHERE 🍜**  
menstagram-aiはMenstagramのラーメン判定API開発のためのリポジトリです。

### 環境構築

```bash
$ git clone https://github.com/uyupun/menstagram-ai.git
$ cd menstagram-ai
$ docker network create menstagram  // menstagram-apiですでに作成している場合は実行しなくて良い
$ make init
```

### コマンド

```bash
$ make up       // 起動
$ make down     // 終了
$ make sh       // bashの起動
```
![PR Status](https://github.com/Makoto-Araki/python_base_image/actions/workflows/pull_request.yaml/badge.svg)
![Main Status](https://github.com/Makoto-Araki/python_base_image/actions/workflows/main_ci.yaml/badge.svg)
![Release Status](https://github.com/Makoto-Araki/python_base_image/actions/workflows/release.yaml/badge.svg)

# python_base_image 基盤イメージ

## 目的
- RPA処理でバージョン管理に細心の注意が必要なパッケージを基盤イメージとして保存

## 開発履歴
| 日付        | バージョン | 説明                                  |
| ---------- | ---------- | ------------------------------------ |
| 2026/03/18 | 1.2.0      | Github ActionsのYAMLファイルの役割分担 |
| 2026/03/14 | 1.1.0      | ベースイメージ更新                     |
| 2026/01/15 | 1.0.0      | 新規作成                              |

## 社内開発環境
- Windows11
- Docker Desktop (Kubernetes有効化 + Dockerhubログイン済)
- VSCode
- WSL
- Github (リモートリポジトリ)
- Dockerhub (Dockerイメージ保存先)

## 前提条件
- Docker Desktopがインストール済でKubernetesクラスタ有効化
- Docker DesktopでDockerhubにログイン済
- Githubにアクセス可
- Dockerhubにアクセス可
- WSL Terminal上で作業 (DevContainer内の作業も存在)
- WSL Terminal上でkubectlが使用可能でKubernetesクラスタ接続可

## CI/CD導入前の開発手順
### 環境構築
```bash
## ディレクトリ作成
$ mkdir python_base_image

## ディレクトリ移動
$ cd python_base_image

## ローカルリポジトリ初期化
$ git init

## メインブランチ設定
$ git branch -M main

## リモートリポジトリ設定
$ git remote add origin git@github.com:Makoto-Araki/python_base_image.git

## Githubのリモートリポジトリからクローン
$ git clone git@github.com:Makoto-Araki/python_base_image.git
```

### 手動デプロイ
```bash
## Dockerイメージをビルド
$ docker build --no-cache -t makotoaraki346/python_base_image_image:X.Y.Z .

## 本番用のDockerイメージをDockerhubにプッシュ
$ docker push makotoaraki346/python_base_image_image:X.Y.Z
```

## CI/CD導入後の開発手順
### 開発用ブランチ作成＋開発作業＋リモートリポジトリへプッシュ
- ブランチ名は feature/******* という名称で統一
- リモートリポジトリ上で issue を作成しておくこと

```bash
## 開発用ブランチ作成
$ git checkout -b feature/*******

## 開発用ブランチ確認
$ git branch

## VSCode起動
$ code .

## ステージング移行
$ git add .

## コミット ※11はissue番号
$ git commit -m "feature/*******(#11)"

## プッシュ
$ git push origin feature/*******
```

### リモートリポジトリ
- プルリクエスト作成
- マージ実行 (mainブランチに統合)

### ブランチ統合
```bash
## ブランチ切替
$ git checkout main

## ブランチ確認
$ git branch

## プル
$ git pull origin main

## 開発ブランチ削除
$ git branch -d feature/*******
```

### リリース
```bash
## タグ作成
$ git tag vX.Y.Z

## リリース
$ git push origin vX.Y.Z
```
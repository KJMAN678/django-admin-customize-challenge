### Install
- mise をインストールする
  - [mise](https://mise.jdx.dev/getting-started.html#installing-mise-cli)

### Claude Code
- GitHub の Settings > Secrets and variables > Actions > New repository secret で ANTHROPIC_API_KEY を追加
- Claude Code の対象リポジトリに追加する

### Command

```sh
# app 追加
$ mkdir web
$ docker compose exec backend django-admin startapp web web

# make migration
$ docker compose exec backend python manage.py makemigrations

http://127.0.0.1:8000/web/

# セキュリティチェック
$ docker compose exec backend djcheckup http://host.docker.internal:8000/web/
```

### Devin

- [Devin's Machine](https://app.devin.ai/workspace) でリポジトリ追加

#### 1.Git Pull
- そのまま

#### 2.Configure Secrets
```sh
# 環境変数用のファイル作成
$ mise make_envrc
```

- ローカル用
```sh
$ brew install direnv
```
#### 4.Maintain Dependencies
```sh
$ docker compose up -d

# コンテナ作り直し
$ mise remake_container
```

#### 5.Set Up Lint
```sh
$ mise lint

- 下記を実行
$ docker compose exec backend ruff check .
$ docker compose exec backend pyrefly check --summarize-errors
$ docker compose exec backend pyrefly check --suppress-errors
$ docker compose exec backend djlint templates/*/*.html --extension=html.j2 --check
$ docker compose exec backend djlint templates/*/*.html --extension=html.j2 --lint

# 修正
$ mise fix

- 下記を実行
$ docker compose exec backend ruff check . --fix
$ docker compose exec backend ruff format .
$ docker compose exec backend djlint templates/*/*.html --extension=html.j2 --reformat
$ docker compose exec backend pyrefly check --remove-unused-ignores
```

#### 6.SetUp Tests
- no tests ran in 0.00s だと Devin の Verify が通らないっぽい
```sh
$ mise test

- 下記を実行
$ docker compose exec backend pytest
```

### 7.Setup Local App

```sh
$ http://localhost:8000/ がアプリケーションのURL
```

#### 8.Additional Notes
- 必ず日本語で回答してください
- Python, Django を利用する
- データベースは Postgres
- テストは pytest を利用する
を入力

### その他
```sh
# コンテナ イメージのサイズを確かめる
$ docker image ls

# docker のセキュリティチェック
$ docker scout quickview <image>:<tag>
$ docker scout cves <image>:<tag>
$ docker scout recommendations <image>:<tag>

# docker の linter
$ hadolint Dockerfile

# インストール可能なLinux ライブラリのバージョンチェックのためにコンテナに入る
$ docker ps
$ docker exec -it devin_django_template-backend-1 bash
$ apt-get update
$ apt-cache policy <library>
```

### 管理コマンド
```sh
$ docker compose exec backend python manage.py query_dummy_data
```

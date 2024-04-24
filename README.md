# KDG 書籍管理システム

KDG のデータベースの授業における API 作成演習用の Python バックエンド。

## 開発環境立ち上げ

```bash
make up
make bash
make install
make seed
make flask-up
```

## アーキテクチャ

設計思想としてリクエストを受け取ってから DB へアクセスし、その結果を受け取りレスポンスを返すプロセスの中でより多くの区間で Pydantic で値を受け渡すことを意識しています。

マイクロフレームワークである flask を使い ORM には SQLAlchemy を使っています。ADR パターンを採用していてコントローラーにはシングルアクションが記述されるようになっています。

ADR パターンですがドメインサービスクラスではなくアプリケーションサービスクラスを設けていて、ドメインという言葉をディレクトリ名などに使わないようにしています。このプロジェクトでは DDD をしないという選択をしています。

## ディレクトリ

* `app/`
  * アプリケーションのコードが入っています。
* `docker/`
  * `docker` から使用するファイルが入っています。
* `app/entity/`
  * `pydantic` 製の Entity や Value Object が入っています。
* `app/error/`
  * `Exception` を継承したエラークラスが入っています。
* `app/migrations/`
  * `alembic` を使用したマイグレーション用のファイルが入っています。
* `app/orm/`
  * `SQLAlchemy` のモデルなどが入っています。
* `app/presentation`
  * `Action` と `Responder` などが入っています。
* `app/repository`
  * `SQLAlchemy` のモデルを使って `Pydantic` のエンティティを返すリポジトリクラスが入っています。
* `app/service`
  * エンティティを使ってリクエストを構築するサービスクラスが入っています。


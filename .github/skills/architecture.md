---
title: "Manage Books プロジェクトアーキテクチャ定義"
category: "reference"
version: "1.0"
last_updated: "2026-02-17"
---

# Manage Books プロジェクトアーキテクチャ

## アーキテクチャスタイル

このプロジェクトは **ADR（Action-Domain-Responder）アーキテクチャパターン** を採用しています。

ADRはMVCの代替パターンで、以下の特徴があります：
- **Action**: コントローラーの役割（リクエスト処理）
- **Domain**: ビジネスロジック（Service + Repository + Entity）
- **Responder**: レスポンス生成（ビューの役割）

## ディレクトリ構造

```
app/
├── presentation/     # プレゼンテーション層 (ADR)
│   └── api/
│       └── user/
│           ├── actions/      # コントローラー役割
│           ├── requests/     # リクエストバリデーション
│           └── responders/   # レスポンス生成
├── service/          # ビジネスロジック層
├── repository/       # データアクセス層
├── entity/           # ドメインモデル層
└── orm/              # ORMモデル層
```

## レイヤー依存ルール

### 依存の方向（一方向のみ許可）

```
presentation → service → repository → entity
                    ↘_____________↗
```

**許可される依存関係**:
- ✅ Action → Service
- ✅ Action → Request
- ✅ Action → Responder
- ✅ Service → Repository（抽象クラス経由）
- ✅ Service → Entity
- ✅ Repository → Entity
- ✅ Repository → ORM

### 禁止される依存関係

❌ entity → repository（EntityがRepositoryを知らない）
❌ entity → service（EntityがServiceを知らない）
❌ entity → presentation（EntityがHTTPを知らない）
❌ repository → service（RepositoryがServiceを知らない）
❌ repository → presentation（RepositoryがHTTPを知らない）
❌ service → presentation（ServiceがHTTPを知らない）

## 各レイヤーの責務

### Entity層（ドメインモデル層）

**責務**: ドメインモデル、データ構造の定義

**許可**:
- Pydantic BaseModelを使用したモデル定義
- IDクラスの定義（BaseId継承）
- 基本的なプロパティ、メソッド
- created_at/updated_atフィールド

**禁止**:
- データベース操作（SQL、ORMクエリ）
- 外部API呼び出し
- HTTPリクエスト処理
- ビジネスロジック（Service層へ委譲）

**例（Good）**:
```python
# entity/user/User.py
from datetime import datetime
from pydantic import BaseModel
from entity.base.BaseId import BaseId

class UserId(BaseId):
    value: int

class User(BaseModel):
    id: UserId
    name: str
    created_at: datetime
    updated_at: datetime
```

**例（Bad）**:
```python
# entity/user/User.py
class User(BaseModel):
    id: UserId
    name: str
    
    def save(self):  # ❌ EntityにDB操作を含めない
        db.session.add(self)
        db.session.commit()
    
    def fetch_from_api(self):  # ❌ Entityに外部API呼び出しを含めない
        response = requests.get(f"/api/users/{self.id}")
        return response.json()
```

---

### Repository層（データアクセス層）

**責務**: データ永続化、データアクセス抽象化

**許可**:
- ORMを使用したデータベース操作
- Entityへの変換（to_entity()メソッド）
- クエリの実行（selectinloadによるEager Loading）
- トランザクション管理（ORMセッション経由）

**禁止**:
- ビジネスロジックの実装（割引計算、バリデーションなど）
- HTTPリクエスト処理
- Service層の呼び出し
- 外部APIの直接呼び出し

**抽象クラスの定義**:
```python
# repository/UserRepository.py
from abc import ABC, abstractmethod
from entity.user.User import User, UserId

class AbstractUserRepository(ABC):
    @abstractmethod
    def find_all(self) -> list[User]:
        raise NotImplementedError

    @abstractmethod
    def find_by_id(self, user_id: UserId) -> User | None:
        raise NotImplementedError

    @abstractmethod
    def create(self, user: User) -> User:
        raise NotImplementedError

    @abstractmethod
    def update(self, user: User) -> User:
        raise NotImplementedError

    @abstractmethod
    def delete(self, user_id: UserId) -> None:
        raise NotImplementedError
```

**具象クラスの実装**:
```python
# repository/UserRepository.py
from orm.models.User import User as UserORM
from sqlalchemy.orm import selectinload

class UserRepository(AbstractUserRepository):
    def find_all(self) -> list[User]:
        users = UserORM.query.all()
        return [user.to_entity() for user in users]

    def find_by_id(self, user_id: UserId) -> User | None:
        user = UserORM.query.filter_by(id=user_id.value).first()
        return user.to_entity() if user else None

    def create(self, user: User) -> User:
        orm_user = UserORM(
            name=user.name,
            created_at=user.created_at,
            updated_at=user.updated_at
        )
        # DB保存処理
        return orm_user.to_entity()
```

**例（Bad）**:
```python
class UserRepository(AbstractUserRepository):
    def create(self, user: User) -> User:
        # ❌ ビジネスロジックをRepositoryに含めない
        if len(user.name) < 3:
            raise ValueError("名前は3文字以上必要です")
        
        # ❌ 割引計算などのビジネスルール
        if user.total > 10000:
            user.total *= 0.9
        
        db.session.add(user)
        db.session.commit()
```

---

### Service層（ビジネスロジック層）

**責務**: ビジネスロジックの実装、ユースケースの調整、トランザクション境界の定義

**許可**:
- リポジトリインターフェースの使用（DI経由）
- ビジネスルールの実装
- トランザクション開始・終了
- 複数のリポジトリの調整
- Entityの生成・更新

**禁止**:
- HTTPリクエスト処理（Requestオブジェクトの使用）
- レスポンス生成（Responderの使用）
- 直接のDB操作（Repositoryを経由）
- 外部APIの直接呼び出し（専用のGateway/Client経由）

**例（Good）**:
```python
# service/UserService.py
from injector import inject
from entity.user.User import User, UserId
from repository.UserRepository import AbstractUserRepository

class UserService:
    @inject
    def __init__(self, repository: AbstractUserRepository):
        self.__repository = repository

    def get_all(self) -> list[User]:
        return self.__repository.find_all()

    def get_by_id(self, user_id: UserId) -> User | None:
        return self.__repository.find_by_id(user_id)

    def create(self, name: str) -> User:
        # ビジネスロジックを実装
        if not name or len(name.strip()) == 0:
            raise ValueError("名前は必須です")
        
        user = User(...)
        return self.__repository.create(user)
```

**例（Bad）**:
```python
class UserService:
    @inject
    def __init__(self, repository: AbstractUserRepository):
        self.__repository = repository

    def create(self, request: CreateUserRequest):  # ❌ HTTPリクエストを受け取らない
        # ビジネスロジック
        db.session.query(UserORM).filter(...).first()  # ❌ 直接DB操作しない
        
        return CreateUserResponder(...)  # ❌ Responderを返さない
```

---

### Presentation層（アクション層）

**責務**: HTTPリクエスト処理、入力検証、レスポンス生成

#### Request（バリデーション）

**責務**: リクエストデータの検証

**許可**:
- Pydanticによるバリデーション
- 入力データの検証（形式チェック）

**禁止**:
- ビジネスロジック（Service層へ）
- DB操作（Repository層へ）

**例**:
```python
# presentation/api/user/requests/create_user.py
from pydantic import BaseModel, ValidationError

class CreateUserRequestData(BaseModel):
    name: str
    value: int | None = None

class CreateUserRequest:
    def __init__(self, request_data: dict):
        self.__request_data = request_data
        self.__validated_data: CreateUserRequestData | None = None

    def validate(self) -> bool:
        try:
            self.__validated_data = CreateUserRequestData(**self.__request_data)
            return True
        except ValidationError:
            return False

    @property
    def data(self) -> CreateUserRequestData:
        if self.__validated_data is None:
            raise ValueError("Request is not validated")
        return self.__validated_data
```

#### Action（コントローラー）

**責務**: HTTPリクエストのハンドリング、Service呼び出し、Responder生成

**許可**:
- HTTPリクエスト/レスポンス処理
- Serviceの呼び出し
- Responderの生成

**禁止**:
- ビジネスロジック（Service層へ）
- 直接のDB操作（Repository層へ）
- バリデーション（Requestクラスへ、adr()で実行）

**例**:
```python
# presentation/api/user/actions/create_user.py
from flask import Response
from injector import inject
from presentation.api.user.requests.create_user import CreateUserRequest
from presentation.api.user.responders.create_user import (
    CreateUserResponder,
    CreateUserResponseDto
)
from service.UserService import UserService

class Action:
    @inject
    def __init__(self, service: UserService):
        self.__service = service

    def execute(self, request: CreateUserRequest) -> Response:
        # サービス呼び出し
        data = request.data
        result = self.__service.create(data.name)

        # レスポンス生成
        dto = CreateUserResponseDto(result)
        responder = CreateUserResponder(dto)
        return responder.getResponse()
```

**例（Bad）**:
```python
class Action:
    def execute(self, request_data: dict):  # ❌ 生の辞書を受け取らない
        # ❌ バリデーションをActionに書かない（adr()で実行）
        if not request_data.get('name'):
            return Response(status=400)
        
        # ❌ ビジネスロジックをActionに書かない
        total = sum(item['price'] for item in request_data['items'])
        
        # ❌ 直接DB操作しない
        user = UserORM(name=request_data['name'])
        db.session.add(user)
        db.session.commit()
```

#### Responder（レスポンス生成）

**責務**: HTTPレスポンスの生成

**許可**:
- DTOの定義（Pydantic BaseModel）
- EntityからDTOへの変換
- JSONシリアライズ

**禁止**:
- ビジネスロジック
- DB操作

**例**:
```python
# presentation/api/user/responders/create_user.py
import json
from flask import Response
from pydantic import BaseModel
from entity.user.User import User

class CreateUserResponseItemDto(BaseModel):
    id: int
    name: str

    def __init__(self, user: User):
        super().__init__(
            id=user.id.value,
            name=user.name
        )

class CreateUserResponseDto(BaseModel):
    data: CreateUserResponseItemDto

    def __init__(self, user: User):
        super().__init__(data=CreateUserResponseItemDto(user))

class CreateUserResponder:
    def __init__(self, dto: CreateUserResponseDto):
        self._dto = dto

    def getResponse(self) -> Response:
        return Response(
            status=200,
            response=json.dumps(self._dto.model_dump()),
            mimetype="application/json"
        )
```

---

## 設計原則

### SOLID原則の適用

- **S**ingle Responsibility: 各クラスは単一の責務
  - Action: HTTP入出力
  - Service: ビジネスロジック
  - Repository: データアクセス
  - Entity: ドメインモデル

- **O**pen/Closed: 拡張に開き、修正に閉じる
  - 抽象クラス（AbstractRepository）を通じて実装を拡張

- **L**iskov Substitution: 派生型は基底型と置換可能
  - UserRepositoryはAbstractUserRepositoryと置換可能

- **I**nterface Segregation: 利用しないインターフェースに依存しない
  - Repositoryは必要なメソッドのみを定義

- **D**ependency Inversion: 抽象に依存、具象に依存しない
  - ServiceはAbstractUserRepositoryに依存（具象UserRepositoryではない）

### 依存性注入（DI）

- `@inject`デコレータを使用して依存を解決
- コンストラクタインジェクションを原則とする
- 抽象クラス（インターフェース）に依存

```python
class UserService:
    @inject
    def __init__(self, repository: AbstractUserRepository):  # ✅ 抽象クラスに依存
        self.__repository = repository
```

### 依存性注入の設定

**ファイル**: `dependency.py`

```python
from repository.UserRepository import (
    AbstractUserRepository,
    UserRepository
)
from service.UserService import UserService

class Dependency:
    @staticmethod
    def config(binder: Binder):
        # Repository
        binder.bind(AbstractUserRepository, to=UserRepository)
        # Service
        binder.bind(UserService, to=UserService)
```

---

## 禁止パターン

### アンチパターン

❌ **God Object**: 全ての責務を持つ巨大クラス
❌ **Anemic Domain Model**: ロジックのないドメインオブジェクト（Entityにロジックを入れない）
❌ **Circular Dependency**: 循環参照（Service A → Service B → Service A）
❌ **Leaky Abstraction**: 実装詳細の漏洩（RepositoryがORMの詳細を露出させない）

### 禁止ライブラリ（レイヤー別）

**Entity層で禁止**:
- `sqlalchemy`, `psycopg2` (DB)
- `requests`, `httpx` (HTTP)
- `flask`, `fastapi` (Webフレームワーク)

**Repository層で禁止**:
- `flask` (Webフレームワーク)

**Service層で禁止**:
- `flask.Request`, `flask.Response`（Webフレームワークの型）
- 直接のDB操作（Repository経由）

---

## 命名規則

| 層 | 命名パターン |
|-----|-------------|
| Entity | `User`, `UserId` |
| Repository | `AbstractUserRepository`, `UserRepository` |
| Service | `UserService` |
| Action | `Action` (クラス名は固定) |
| Request | `CreateUserRequest`, `CreateUserRequestData` |
| Responder | `CreateUserResponder`, `CreateUserResponseDto` |

---

## ディレクトリ構造テンプレート

新しい機能を追加する場合:

```
entity/
└── user/
    ├── __init__.py
    ├── User.py
    ├── UserId.py
    └── related/
        └── RelatedUser.py

repository/
├── AbstractUserRepository.py
└── UserRepository.py

service/
└── UserService.py

presentation/api/user/
├── actions/
│   ├── __init__.py
│   ├── get_list.py
│   ├── get_detail.py
│   └── create_user.py
├── requests/
│   ├── __init__.py
│   ├── get_list.py
│   └── create_user.py
└── responders/
    ├── __init__.py
    ├── get_list.py
│   └── create_user.py
```

---

## チェックリスト

レビュー時は以下を確認：

### 構造チェック
- [ ] ファイルが適切なレイヤーに配置されているか
- [ ] 依存関係が一方向（Presentation → Service → Repository → Entity）か
- [ ] 各レイヤーの責務を越えていないか

### コードチェック
- [ ] Entity層にインフラコード（DB、HTTP）が含まれていないか
- [ ] Repository層にビジネスロジックが混入していないか
- [ ] Service層がHTTP処理をしていないか
- [ ] Action層がビジネスロジックを実装していないか
- [ ] リポジトリパターンが正しく使われているか（抽象クラス経由）
- [ ] 依存性注入（DI）が適切に使われているか（@injectデコレータ）

### 設計チェック
- [ ] SOLID原則に違反していないか
- [ ] 循環依存が発生していないか
- [ ] 適切な抽象化レベルか
- [ ] 命名規則に従っているか

---

## テスト

基本はE2Eテストだけでよく、Serviceロジックが複雑であればRepositoryをモックしてServiceロジックのテストを書く。

```python
# Serviceのテスト例
class TestUserService:
    def test_create_user_success(self):
        # Arrange
        mock_repo = Mock(AbstractUserRepository)
        mock_repo.create.return_value = User(id=UserId(1), name="Test")
        service = UserService(mock_repo)
        
        # Act
        result = service.create("Test")
        
        # Assert
        assert result.name == "Test"
        mock_repo.create.assert_called_once()
```

---

## 参考資料

- ADR Pattern: https://matthewpaulthomas.com/adr-pattern/
- SOLID Principles: https://en.wikipedia.org/wiki/SOLID
- Dependency Injection: https://python-dependency-injector.ets-labs.org/
- Clean Architecture: https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html

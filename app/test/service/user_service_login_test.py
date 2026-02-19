import re
from datetime import datetime, timedelta

import pytest
from bcrypt import gensalt, hashpw

from entity.session import CreateSession
from entity.user import User, UserId
from error.auth import InvalidPasswordException
from service.UserService import UserService


class FakeUserRepository:
    def __init__(self, user: User):
        self.user = user
        self.last_email = None

    def find_by_email(self, email: str) -> User:
        self.last_email = email
        return self.user


class FakeSessionRepository:
    def __init__(self):
        self.created_session: CreateSession | None = None

    def create_session(self, session: CreateSession):
        self.created_session = session


def build_user(password: str) -> User:
    hashed = hashpw(password.encode(), gensalt()).decode()
    return User(
        id=UserId(value=1),
        name="user1",
        email="user1@vantan.jp",
        password=hashed
    )


def test_login_success_creates_session_and_returns_dto():
    user = build_user("password1")
    user_repo = FakeUserRepository(user)
    session_repo = FakeSessionRepository()

    service = UserService(user_repo, session_repo)

    dto = service.login("user1@vantan.jp", "password1")

    assert user_repo.last_email == "user1@vantan.jp"
    assert re.fullmatch(r"[0-9a-f]{64}", dto.token)

    expired_at = datetime.fromisoformat(dto.expired_at)
    now = datetime.now()
    assert expired_at >= now
    assert expired_at <= now + timedelta(days=31)

    assert session_repo.created_session is not None
    created = session_repo.created_session
    assert created.user_id == user.id
    assert created.token == dto.token
    assert created.expired_at >= now


def test_login_invalid_password_raises_and_does_not_create_session():
    user = build_user("password1")
    user_repo = FakeUserRepository(user)
    session_repo = FakeSessionRepository()

    service = UserService(user_repo, session_repo)

    with pytest.raises(InvalidPasswordException):
        service.login("user1@vantan.jp", "invalid_password")

    assert session_repo.created_session is None
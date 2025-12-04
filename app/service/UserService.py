from datetime import datetime, timedelta
from hashlib import sha256
from time import time

from bcrypt import checkpw
from entity.session import CreateSession
from entity.user import UserId
from error.auth import InvalidPasswordException
from injector import inject
from presentation.api.user.responders import get_user, login
from repository.SessionRepository import AbstractSessionRepository
from repository.UserRepository import AbstractUserRepository


class UserService:
    @inject
    def __init__(self,
                 user_repository: AbstractUserRepository,
                 session_repository: AbstractSessionRepository
                 ):
        self.__user_repository = user_repository
        self.__session_repository = session_repository

    def get_user(self, user_id: UserId) -> get_user.GetUserResponseDto:
        user = self.__user_repository.find_by_id(user_id)
        return get_user.GetUserResponseDto(user)

    def login(self, email: str, password: str)-> login.LoginResponseDto:
        user = self.__user_repository.find_by_email(email)
        validPassword = checkpw(password.encode(), user.password.encode())
        if not validPassword:
            raise InvalidPasswordException
        token = sha256(string=f"{user.id.value}-{time()}".encode()).hexdigest()
        expired_at = datetime.now() + timedelta(days=30)
        self.__session_repository.create_session(CreateSession(
            token=token,
            user_id=user.id,
            expired_at=expired_at
        ))
        return login.LoginResponseDto(
            token=token,
            expired_at=str(expired_at)
        )

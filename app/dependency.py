from injector import Binder, Injector
from repository.BookCategoryRepository import (
    AbstractBookCategoryRepository,
    BookCategoryRepository,
)
from repository.SessionRepository import AbstractSessionRepository, SessionRepository
from repository.UserRepository import AbstractUserRepository, UserRepository
from service.UserService import UserService


class Dependency:
    def __init__(self) -> None:
        self.injector = Injector(self.config)

    @staticmethod
    def config(binder: Binder):
        # repository
        binder.bind(AbstractUserRepository, to=UserRepository)
        binder.bind(AbstractSessionRepository, to=SessionRepository)
        binder.bind(AbstractBookCategoryRepository, to=BookCategoryRepository)
        # service
        binder.bind(UserService, to=UserService)

    def resolve(self, cls):
        return self.injector.get(cls)

di = Dependency()

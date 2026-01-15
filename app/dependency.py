from injector import Binder, Injector
from repository.BookRepository import AbstractBookRepository, BookRepository
from repository.BookCategoryRepository import (
    AbstractBookCategoryRepository,
    BookCategoryRepository,
)
from repository.SessionRepository import AbstractSessionRepository, SessionRepository
from repository.UserRepository import AbstractUserRepository, UserRepository
from service.BookService import BookService
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
        binder.bind(AbstractBookRepository, to=BookRepository)
        # service
        binder.bind(UserService, to=UserService)
        binder.bind(BookService, to=BookService)

    def resolve(self, cls):
        return self.injector.get(cls)

di = Dependency()

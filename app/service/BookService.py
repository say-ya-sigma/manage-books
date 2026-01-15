from typing import TYPE_CHECKING

from injector import inject
from repository.BookRepository import AbstractBookRepository

if TYPE_CHECKING:
    from presentation.api.book.responders.get_books import GetBooksResponseDto


class BookService:
    @inject
    def __init__(self, book_repository: AbstractBookRepository):
        self.__book_repository = book_repository

    def get_books(self) -> "GetBooksResponseDto":
        from presentation.api.book.responders.get_books import GetBooksResponseDto

        books = self.__book_repository.find_all_with_category()
        return GetBooksResponseDto(books)

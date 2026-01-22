from entity.book.BookId import BookId
from entity.book.category.BookCategoryId import BookCategoryId
from injector import inject
from repository.BookRepository import AbstractBookRepository


class BookService:
    @inject
    def __init__(self, book_repository: AbstractBookRepository):
        self.__book_repository = book_repository

    def get_books(self):
        books = self.__book_repository.find_all_with_category()
        return books

    def get_book(self, book_id: BookId):
        book = self.__book_repository.find_by_id(book_id)
        return book

    def get_books_by_category_id(self, category_id: BookCategoryId):
        books = self.__book_repository.find_by_category_id(category_id)
        return books
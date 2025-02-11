from entity.book.category import BookCategoryId
from injector import inject
from presentation.api.book.category.responders import create_category, get_category
from repository.BookCategoryRepository import AbstractBookCategoryRepository


class BookCategoryService:
    @inject
    def __init__(self, book_category_repository: AbstractBookCategoryRepository):
        self.__book_category_repository = book_category_repository

    def get_book_category(
        self,
        book_category_id: BookCategoryId
    ) -> get_category.GetCategoryResponseDto:
        book_category = self.__book_category_repository.find_by_id(book_category_id)
        return get_category.GetCategoryResponseDto(book_category)

    def create_book_category(
        self,
        name: str
    ) -> create_category.CreateCategoryResponseDto:
        book_category_id = self.__book_category_repository.create(name)
        return create_category.CreateCategoryResponseDto(book_category_id)

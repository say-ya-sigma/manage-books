from entity.book.category.BookCategoryId import BookCategoryId
from injector import inject
from presentation.api.book.category.responders.get_category import (
    GetCategoryResponseDto,
)
from repository.BookCategoryRepository import AbstractBookCategoryRepository


class BookCategoryService:
    @inject
    def __init__(self, book_category_repository: AbstractBookCategoryRepository):
        self._book_category_repository = book_category_repository

    def get_book_category(
        self,
        book_category_id: BookCategoryId
    ) -> GetCategoryResponseDto:
        book_category = self._book_category_repository.find_by_id(book_category_id)
        return GetCategoryResponseDto(book_category)

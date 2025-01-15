from abc import ABC, abstractmethod

from entity.book.category import BookCategory as EntityBookCategory
from entity.book.category import BookCategoryId
from error.common import NotFoundException
from orm.models.BookCategory import BookCategory


class AbstractBookCategoryRepository(ABC):
    @abstractmethod
    def find_by_id(self, id: BookCategoryId) -> EntityBookCategory:
        raise NotImplementedError


class BookCategoryRepository(AbstractBookCategoryRepository):
    def find_by_id(self, id: BookCategoryId):
        book_category = BookCategory.query.filter(BookCategory.id == id.value).first()
        if book_category is None:
            raise NotFoundException()
        return book_category.to_entity()

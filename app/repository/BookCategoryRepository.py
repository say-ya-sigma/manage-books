from abc import ABC, abstractmethod

from entity.book.category import BookCategory as EntityBookCategory
from entity.book.category import BookCategoryId
from error.common import NotFoundException
from orm.models.BookCategory import BookCategory


class AbstractBookCategoryRepository(ABC):
    @abstractmethod
    def find_by_id(self, id: BookCategoryId) -> EntityBookCategory:
        raise NotImplementedError
    @abstractmethod
    def create(self, name: str) -> BookCategoryId:
        raise NotImplementedError
    @abstractmethod
    def update(self, id: BookCategoryId, name: str) -> None:
        raise NotImplementedError
    @abstractmethod
    def delete(self, id: BookCategoryId) -> None:
        raise NotImplementedError


class BookCategoryRepository(AbstractBookCategoryRepository):
    def find_by_id(self, id: BookCategoryId):
        book_category = BookCategory.query.filter(BookCategory.id == id.value).first()
        if book_category is None:
            raise NotFoundException()
        return book_category.to_entity()

    def create(self, name):
        book_category = BookCategory(name=name)
        book_category.save()
        return book_category.to_entity().id

    def update(self, id, name):
        book_category = BookCategory.query.filter(BookCategory.id == id.value).first()
        if book_category is None:
            raise NotFoundException()

        book_category.name = name
        book_category.save()

    def delete(self, id):
        book_category = BookCategory.query.filter(BookCategory.id == id.value).first()
        if book_category is None:
            raise NotFoundException()

        book_category.delete()

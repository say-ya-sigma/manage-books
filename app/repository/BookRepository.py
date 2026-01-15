from abc import ABC, abstractmethod

from entity.book import BookWithCategory
from orm.models.Book import Book
from sqlalchemy.orm import joinedload


class AbstractBookRepository(ABC):
    @abstractmethod
    def find_all_with_category(self) -> list[BookWithCategory]:
        raise NotImplementedError


class BookRepository(AbstractBookRepository):
    def find_all_with_category(self) -> list[BookWithCategory]:
        books = Book.query.options(joinedload(Book.book_category)).all()
        return [
            BookWithCategory(
                id=book.to_entity().id,
                title=book.title,
                author=book.author,
                isbn=book.isbn,
                publisher=book.publisher,
                book_category_id=book.book_category_id,
                book_category_name=(
                    book.book_category.name if book.book_category else None
                ),
                created_at=book.created_at,
                updated_at=book.updated_at,
            )
            for book in books
        ]
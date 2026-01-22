from abc import ABC, abstractmethod

from entity.book import BookWithCategory
from entity.book.BookId import BookId
from entity.book.category.BookCategoryId import BookCategoryId
from orm.models.Book import Book
from sqlalchemy.orm import selectinload


class AbstractBookRepository(ABC):
    @abstractmethod
    def find_all_with_category(self) -> list[BookWithCategory]:
        raise NotImplementedError

    @abstractmethod
    def find_by_id(self, book_id: BookId) -> BookWithCategory | None:
        raise NotImplementedError

    @abstractmethod
    def find_by_category_id(self, category_id: BookCategoryId) -> list[BookWithCategory]:
        raise NotImplementedError


class BookRepository(AbstractBookRepository):
    def find_all_with_category(self) -> list[BookWithCategory]:
        books = Book.query.options(selectinload(Book.book_category)).all()
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

    def find_by_id(self, book_id: BookId) -> BookWithCategory | None:
        book = Book.query.options(selectinload(Book.book_category)).filter_by(
            id=book_id.value
        ).first()
        if book is None:
            return None
        return BookWithCategory(
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

    def find_by_category_id(self, category_id: BookCategoryId) -> list[BookWithCategory]:
        books = Book.query.options(selectinload(Book.book_category)).filter_by(
            book_category_id=category_id.value
        ).all()
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

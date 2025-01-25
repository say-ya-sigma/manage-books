from entity.book import Book as EntityBook
from entity.book import BookId
from orm.models.BookCategory import BookCategory
from orm.settings import Base
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import (
    Mapped,
    MappedAsDataclass,
    mapped_column,
    relationship,
)


class Book(MappedAsDataclass, Base):
    __tablename__ = "books"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(255))
    author: Mapped[str] = mapped_column(String(255))
    isbn: Mapped[str] = mapped_column(String(13))  # ISBN is usually 13 characters long
    publisher: Mapped[str] = mapped_column(String(255))
    book_category_id: Mapped[int] = mapped_column(
        ForeignKey("book_categories.id", ondelete="set null"), nullable=True
    )

    book_category: Mapped["BookCategory"] = relationship(
        "BookCategory",
        backref="books"
    )

    def to_entity(self):
        return EntityBook(
            id=BookId(value=self.id),
            title=self.title,
            author=self.author,
            isbn=self.isbn,
            publisher=self.publisher,
            book_category_id=self.book_category_id,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )

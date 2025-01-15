from entity.book.category.BookCategory import BookCategory as EntityBookCategory
from entity.book.category.BookCategoryId import BookCategoryId
from orm.settings import Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped, MappedAsDataclass, mapped_column


class BookCategory(MappedAsDataclass, Base):
    __tablename__ = "book_categories"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))

    def to_entity(self):
        return EntityBookCategory(
            id=BookCategoryId(value=self.id),
            name=self.name,
            created_at=self.created_at,
            updated_at=self.updated_at
        )

from orm.settings import Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped, MappedAsDataclass, mapped_column


class BookCategory(MappedAsDataclass, Base):
    __tablename__ = "book_categories"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))

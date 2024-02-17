from sqlalchemy import String
from sqlalchemy.orm import Mapped, MappedAsDataclass, mapped_column

from orm.settings import Base


class User(MappedAsDataclass, Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    email: Mapped[str] = mapped_column(String(255))
    password: Mapped[str] = mapped_column(String(255))

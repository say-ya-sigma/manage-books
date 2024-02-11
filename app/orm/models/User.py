from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from settings import Base, engine

class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    email: Mapped[str] = mapped_column(String(255))
    password: Mapped[str] = mapped_column(String(255))

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
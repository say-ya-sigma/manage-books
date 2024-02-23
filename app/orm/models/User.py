from entity.user.User import User as EntityUser
from entity.user.UserId import UserId
from orm.settings import Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped, MappedAsDataclass, mapped_column


class User(MappedAsDataclass, Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    email: Mapped[str] = mapped_column(String(255))
    password: Mapped[str] = mapped_column(String(255))

    def to_entity(self):
        return EntityUser(
            id=UserId(self.id),
            name=self.name,
            email=self.email,
            password=self.password,
        )

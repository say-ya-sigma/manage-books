from datetime import datetime

from entity.session import Session as EntitySession
from entity.session import SessionId
from entity.user import UserId
from orm.settings import Base
from sqlalchemy import DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, MappedAsDataclass, mapped_column


class Session(MappedAsDataclass, Base):
    __tablename__ = "sessions"
    id: Mapped[int] = mapped_column(primary_key=True, init=False)
    token: Mapped[str] = mapped_column(String(64))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="cascade"))
    expired_at: Mapped[datetime] = mapped_column(DateTime)

    def to_entity(self) -> EntitySession:
        return EntitySession(
            id=SessionId(value=self.id),
            token=self.token,
            user_id=UserId(value=self.user_id),
            expired_at=self.expired_at
        )

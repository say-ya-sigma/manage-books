from datetime import datetime

from entity.user.UserId import UserId
from pydantic import BaseModel

from .SessionId import SessionId


class Session(BaseModel):
    id: SessionId
    token: str
    user_id: UserId
    expired_at: datetime

    def isExpired(self) -> bool:
        return self.expired_at > datetime.now()

class CreateSession(BaseModel):
    token: str
    user_id: UserId
    expired_at: datetime

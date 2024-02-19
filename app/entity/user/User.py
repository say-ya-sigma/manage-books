from pydantic import BaseModel

from .UserId import UserId


class User(BaseModel):
    id: UserId
    name: str
    email: str
    password: str

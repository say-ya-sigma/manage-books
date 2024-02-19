from flask import Request
from pydantic import BaseModel

from entity.user.UserId import UserId
from presentation.abstract.adr import AbstractRequest


class GetUserRequest(BaseModel):
    user_id: UserId

class Request(AbstractRequest):
    def __init__(self, request: Request, id: int):
        self._request = request
        self._id = id

    def validate(self) -> bool:
        self.get_user_request = GetUserRequest(
            user_id=UserId(self._id)
        )

        return True


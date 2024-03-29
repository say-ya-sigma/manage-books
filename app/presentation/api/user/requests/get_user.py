from entity.user.UserId import UserId
from flask import Request
from pydantic import BaseModel


class GetUserRequestDto(BaseModel):
    user_id: UserId

class GetUserRequest:
    def __init__(self, request: Request, id: int):
        self._request = request
        self._id = id

    def validate(self) -> bool:
        self.get_user_request = GetUserRequestDto(
            user_id=UserId(value=self._id)
        )

        return True


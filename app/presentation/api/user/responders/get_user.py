import json

from entity.user.User import User
from flask import Response
from pydantic import BaseModel


class GetUserResponseDto(BaseModel):
    id: int
    name: str
    email: str
    def __init__(self, user: User):
        super().__init__(
            id=user.id.value,
            name=user.name,
            email=user.email
        )

class GetUserResponder:
    dto: GetUserResponseDto
    def __init__(self, dto: GetUserResponseDto):
        self._dto = dto

    def getResponse(self) -> Response:
        return Response(
            status=200,
            response=json.dumps(self._dto.model_dump()),
            mimetype="application/json"
        )

import json

from flask import Response
from pydantic import BaseModel


class LoginResponseDto(BaseModel):
    token: str
    expired_at: str
    def __init__(self, token: str, expired_at: str):
        super().__init__(
            token=token,
            expired_at=expired_at
        )

class LoginResponder:
    dto: LoginResponseDto
    def __init__(self, dto: LoginResponseDto):
        self._dto = dto

    def getResponse(self) -> Response:
        return Response(
            status=200,
            response=json.dumps(self._dto.model_dump()),
            mimetype="application/json"
        )

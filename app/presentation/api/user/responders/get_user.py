import json

from entity.user.User import User
from flask import Response
from pydantic import BaseModel


class GetUserResponder(BaseModel):
    id: int
    name: str
    email: str
    def __init__(self, user: User):
        super().__init__(
            id=user.id.value,
            name=user.name,
            email=user.email
        )

    @property
    def response(self) -> Response:
        return Response(
            status=200,
            response=json.dumps(self.model_dump()),
            mimetype="application/json"
        )

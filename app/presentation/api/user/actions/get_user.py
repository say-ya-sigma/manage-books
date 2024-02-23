import json

from flask import Response
from injector import inject
from presentation.api.user.requests.get_user import GetUserRequest
from service.UserService import UserService


class Action:
    @inject
    def __init__ (self, user_service: UserService):
        self._user_service = user_service

    def execute(self, request: GetUserRequest) -> Response:

        user = self._user_service.get_user(request.get_user_request.user_id)
        return Response(
            status=200,
            response=json.dumps(user.model_dump()),
            mimetype="application/json"
        )


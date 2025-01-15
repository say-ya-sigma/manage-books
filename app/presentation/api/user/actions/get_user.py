from flask import Response
from injector import inject
from presentation.api.user.requests.get_user import GetUserRequest
from presentation.api.user.responders.get_user import GetUserResponder
from service.UserService import UserService


class Action:
    @inject
    def __init__ (self, user_service: UserService):
        self.__user_service = user_service

    def execute(self, request: GetUserRequest) -> Response:

        user = self.__user_service.get_user(request.user_id)
        responder = GetUserResponder(user)
        return responder.getResponse()


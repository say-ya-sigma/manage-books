from flask import Response
from injector import inject
from presentation.api.user.requests.login import LoginRequest
from presentation.api.user.responders.login import LoginResponder
from service.UserService import UserService


class Action:
    @inject
    def __init__ (self, user_service: UserService):
        self.__user_service = user_service

    def execute(self, request: LoginRequest) -> Response:

        dto = self.__user_service.login(request.email, request.password)
        responder = LoginResponder(dto)
        return responder.getResponse()


from entity.user.UserId import UserId
from flask import Request


class GetUserRequest:
    def __init__(self, request: Request, id: int):
        self.__request = request
        self.__id = id

    def validate(self) -> bool:
        try:
            self.__user_id = UserId(value=self.__id)
        except ValueError as e:
            print(e)
            return False

        return True

    @property
    def user_id(self):
        return self.__user_id


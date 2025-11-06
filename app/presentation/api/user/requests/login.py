from flask import Request


class LoginRequest:
    def __init__(self, request: Request):
        self.__request = request

    def validate(self) -> bool:
        json = self.__request.get_json()
        if not json or "email" not in json or "password" not in json:
            print("Invalid request")
            return False
        self.__email: str = json["email"]
        self.__password: str = json["password"]

        return True

    @property
    def email(self):
        return self.__email

    @property
    def password(self):
        return self.__password

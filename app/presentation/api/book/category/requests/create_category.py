from flask import Request


class CreateCategoryRequest:
    def __init__(self, request: Request):
        self.__request = request

    def validate(self) -> bool:
        json = self.__request.get_json()
        if not json or "name" not in json or not isinstance(json["name"], str):
            print("Invalid request")
            return False
        self.__name: str = json["name"]
        return True

    @property
    def name(self) -> str:
        return self.__name

from flask import Request


class UpdateCategoryRequest:
    def __init__(self, request: Request):
        self.__request = request

    def validate(self) -> bool:
        json = self.__request.get_json()
        if not json:
            print("Invalid request")
            return False
        existId = "book_category_id" in json and isinstance(json["book_category_id"], int)
        existName = "name" in json and isinstance(json["name"], str)
        if not existId or not existName:
            print("Invalid request")
            return False
        self.__name: str = json["name"]
        self.__book_category_id: int = json["book_category_id"]
        return True

    @property
    def name(self) -> str:
        return self.__name

    @property
    def book_category_id(self) -> int:
        return self.__book_category_id

from flask import Request


class DeleteCategoryRequest:
    def __init__(self, request: Request):
        self.__request = request

    def validate(self) -> bool:
        json = self.__request.get_json()
        if not json or "book_category_id" not in json or not isinstance(json["book_category_id"], int):
            print("Invalid request")
            return False
        self.__book_category_id: int = json["book_category_id"]
        return True

    @property
    def book_category_id(self) -> int:
        return self.__book_category_id

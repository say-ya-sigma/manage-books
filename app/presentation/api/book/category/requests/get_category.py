from entity.book.category import BookCategoryId
from flask import Request


class GetCategoryRequest:
    def __init__(self, request: Request, id: int):
        self.__request = request
        self.__id = id

    def validate(self) -> bool:
        try:
            self.__book_category_id = BookCategoryId(value=self.__id)
        except ValueError as e:
            print(e)
            return False

        return True

    @property
    def book_category_id(self) -> BookCategoryId:
        return self.__book_category_id

from entity.book.BookId import BookId
from flask import Request


class GetBookRequest:
    def __init__(self, request: Request, id: int):
        self.__request = request
        self.__id = id

    def validate(self) -> bool:
        try:
            self.__book_id = BookId(value=self.__id)
        except ValueError as e:
            print(e)
            return False

        return True

    @property
    def book_id(self) -> BookId:
        return self.__book_id

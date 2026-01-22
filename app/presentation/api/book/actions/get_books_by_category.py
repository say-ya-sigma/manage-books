from flask import Response
from injector import inject
from presentation.api.book.requests.get_books_by_category import GetBooksByCategoryRequest
from presentation.api.book.responders.get_books_by_category import (
    GetBooksByCategoryResponder,
    GetBooksByCategoryResponseDto,
)
from service.BookService import BookService


class Action:
    @inject
    def __init__(self, book_service: BookService):
        self.__book_service = book_service

    def execute(self, request: GetBooksByCategoryRequest) -> Response:
        books = self.__book_service.get_books_by_category_id(request.category_id)
        dto = GetBooksByCategoryResponseDto(books)
        responder = GetBooksByCategoryResponder(dto)
        return responder.getResponse()

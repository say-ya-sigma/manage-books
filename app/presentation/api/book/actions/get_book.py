from flask import Response
from injector import inject
from presentation.api.book.requests.get_book import GetBookRequest
from presentation.api.book.responders.get_book import (
    GetBookResponder,
    GetBookResponseDto,
)
from service.BookService import BookService


class Action:
    @inject
    def __init__(self, book_service: BookService):
        self.__book_service = book_service

    def execute(self, request: GetBookRequest) -> Response:
        book = self.__book_service.get_book(request.book_id)
        if book is None:
            return Response(status=404)
        dto = GetBookResponseDto(book)
        responder = GetBookResponder(dto)
        return responder.getResponse()

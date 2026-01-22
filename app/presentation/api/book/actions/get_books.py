from flask import Response
from injector import inject
from presentation.api.book.requests.get_books import GetBooksRequest
from presentation.api.book.responders.get_books import GetBooksResponder, GetBooksResponseDto
from service.BookService import BookService


class Action:
    @inject
    def __init__(self, book_service: BookService):
        self.__book_service = book_service

    def execute(self, request: GetBooksRequest) -> Response:
        books = self.__book_service.get_books()
        dto = GetBooksResponseDto(books)
        responder = GetBooksResponder(dto)
        return responder.getResponse()
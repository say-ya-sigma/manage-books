from flask import Response
from injector import inject
from presentation.api.book.requests.get_books import GetBooksRequest
from presentation.api.book.responders.get_books import GetBooksResponder
from service.BookService import BookService


class Action:
    @inject
    def __init__(self, book_service: BookService):
        self.__book_service = book_service

    def execute(self, request: GetBooksRequest) -> Response:
        books = self.__book_service.get_books()
        responder = GetBooksResponder(books)
        return responder.getResponse()
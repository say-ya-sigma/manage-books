from flask import Response
from injector import inject
from presentation.api.book.category.requests.create_category import (
    CreateCategoryRequest,
)
from presentation.api.book.category.responders.create_category import (
    CreateCategoryResponder,
)
from service.BookCategoryService import BookCategoryService


class Action:
    @inject
    def __init__ (self, book_category_service: BookCategoryService):
        self.__book_category_service = book_category_service

    def execute(self, request: CreateCategoryRequest) -> Response:

        book_category_id = self.__book_category_service.create_book_category(
            request.name
        )
        responder = CreateCategoryResponder(book_category_id)
        return responder.getResponse()


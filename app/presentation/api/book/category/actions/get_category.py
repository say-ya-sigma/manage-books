from flask import Response
from injector import inject
from presentation.api.book.category.requests.get_category import GetCategoryRequest
from presentation.api.book.category.responders.get_category import GetCategoryResponder
from service.BookCategoryService import BookCategoryService


class Action:
    @inject
    def __init__ (self, book_category_service: BookCategoryService):
        self.__book_category_service = book_category_service

    def execute(self, request: GetCategoryRequest) -> Response:

        book_category = self.__book_category_service.get_book_category(
            request.book_category_id
        )
        responder = GetCategoryResponder(book_category)
        return responder.getResponse()

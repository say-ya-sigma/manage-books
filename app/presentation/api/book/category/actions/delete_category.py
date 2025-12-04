from entity.book.category.BookCategoryId import BookCategoryId
from flask import Response
from injector import inject
from presentation.api.book.category.requests.delete_category import (
    DeleteCategoryRequest,
)
from service.BookCategoryService import BookCategoryService


class Action:
    @inject
    def __init__ (self, book_category_service: BookCategoryService):
        self.__book_category_service = book_category_service

    def execute(self, request: DeleteCategoryRequest) -> Response:
        self.__book_category_service.delete_book_category(
            BookCategoryId(value=request.book_category_id)
        )
        return Response(
            status=200,
            response=None,
            mimetype="application/json"
        )

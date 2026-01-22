import json

from entity.book import BookWithCategory
from flask import Response
from pydantic import BaseModel


class BookItemDto(BaseModel):
    id: int
    title: str
    author: str
    isbn: str
    publisher: str
    book_category_id: int | None
    book_category_name: str | None

    def __init__(self, book: BookWithCategory):
        super().__init__(
            id=book.id.value,
            title=book.title,
            author=book.author,
            isbn=book.isbn,
            publisher=book.publisher,
            book_category_id=book.book_category_id,
            book_category_name=book.book_category_name,
        )


class GetBooksByCategoryResponseDto(BaseModel):
    books: list[BookItemDto]

    def __init__(self, books: list[BookWithCategory]):
        super().__init__(books=[BookItemDto(book) for book in books])


class GetBooksByCategoryResponder:
    def __init__(self, dto: GetBooksByCategoryResponseDto):
        self._dto = dto

    def getResponse(self) -> Response:
        return Response(
            status=200,
            response=json.dumps(self._dto.model_dump()),
            mimetype="application/json",
        )

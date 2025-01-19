import json

from entity.book.category import BookCategory
from flask import Response
from pydantic import BaseModel


class GetCategoryResponseDto(BaseModel):
    id: int
    name: str
    def __init__(self, book_category: BookCategory):
        super().__init__(
            id=book_category.id.value,
            name=book_category.name
        )

class GetCategoryResponder:
    def __init__(self, dto: GetCategoryResponseDto):
        self._dto = dto

    def getResponse(self) -> Response:
        return Response(
            status=200,
            response=json.dumps(self._dto.model_dump()),
            mimetype="application/json"
        )

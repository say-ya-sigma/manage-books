import json

from entity.book.category import BookCategoryId
from flask import Response
from pydantic import BaseModel


class CreateCategoryResponseDto(BaseModel):
    id: int
    def __init__(self, book_category_id: BookCategoryId):
        super().__init__(
            id=book_category_id.value,
        )

class CreateCategoryResponder:
    def __init__(self, dto: CreateCategoryResponseDto):
        self._dto = dto

    def getResponse(self) -> Response:
        return Response(
            status=200,
            response=json.dumps(self._dto.model_dump()),
            mimetype="application/json"
        )

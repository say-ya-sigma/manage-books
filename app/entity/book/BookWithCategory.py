from datetime import datetime

from pydantic import BaseModel

from .BookId import BookId


class BookWithCategory(BaseModel):
    id: BookId
    title: str
    author: str
    isbn: str
    publisher: str
    book_category_id: int | None
    book_category_name: str | None
    created_at: datetime
    updated_at: datetime

from datetime import datetime

from pydantic import BaseModel

from .BookId import BookId


class Book(BaseModel):
    id: BookId
    title: str
    author: str
    isbn: str
    publisher: str
    book_category_id: int
    created_at: datetime
    updated_at: datetime

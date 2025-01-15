from datetime import datetime

from pydantic import BaseModel

from .BookCategoryId import BookCategoryId


class BookCategory(BaseModel):
    id: BookCategoryId
    name: str
    created_at: datetime
    updated_at: datetime

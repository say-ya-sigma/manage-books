from pydantic import BaseModel, Field


class BaseId(BaseModel, frozen=True):
    value: int = Field(ge=1)

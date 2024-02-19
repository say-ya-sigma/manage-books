from pydantic import Field, RootModel


class UserId(RootModel):
    root: int = Field(..., ge=1)

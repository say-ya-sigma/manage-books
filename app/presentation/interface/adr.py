from typing import Protocol

from flask import Request, Response


class AdrRequest(Protocol):
    def __init__(self, request: Request, **kwargs) -> None:
        raise NotImplementedError
    def validate(self) -> bool:
        raise NotImplementedError

class AdrAction(Protocol):
    def execute(self, request: AdrRequest) -> Response:
        raise NotImplementedError


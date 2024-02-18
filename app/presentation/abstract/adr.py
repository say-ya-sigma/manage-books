
from abc import ABC, abstractmethod

from flask import Request, Response


class AbstractRequest(ABC):
    @abstractmethod
    def __init__(self, request: Request, **path_params):
        raise NotImplementedError
    @abstractmethod
    def validate(self) -> bool:
        raise NotImplementedError

class AbstractAction(ABC):
    @abstractmethod
    def execute(self, request: AbstractRequest) -> Response:
        raise NotImplementedError


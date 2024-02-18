import json

from flask import Response

from presentation.abstract.adr import AbstractAction, AbstractRequest


class Action(AbstractAction):
    def execute(self, request: AbstractRequest) -> Response:
        return Response(
            status=200,
            response=json.dumps({"message": "Hello, world!"}),
        )

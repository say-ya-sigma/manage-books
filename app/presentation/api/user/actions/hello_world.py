import json

from flask import Response
from presentation.api.user.requests.hello_world import HelloWorldRequest


class Action:
    def execute(self, request: HelloWorldRequest) -> Response:
        return Response(
            status=200,
            response=json.dumps({"message": "Hello, world!"}),
        )

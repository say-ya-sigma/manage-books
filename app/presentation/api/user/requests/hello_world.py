from presentation.abstract.adr import AbstractRequest


class Request(AbstractRequest):
    def __init__(self, request):
        self._request = request
    def validate(self):
        return False

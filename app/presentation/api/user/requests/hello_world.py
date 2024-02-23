class HelloWorldRequest:
    def __init__(self, request):
        self._request = request
    def validate(self):
        return True

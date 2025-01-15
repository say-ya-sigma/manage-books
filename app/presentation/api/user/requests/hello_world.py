class HelloWorldRequest:
    def __init__(self, request):
        self.__request = request
    def validate(self):
        return True

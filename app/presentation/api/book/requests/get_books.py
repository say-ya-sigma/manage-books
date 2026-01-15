class GetBooksRequest:
    def __init__(self, request):
        self.__request = request

    def validate(self) -> bool:
        return True
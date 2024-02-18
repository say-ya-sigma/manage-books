from functools import wraps

from werkzeug.exceptions import UnprocessableEntity

from presentation.abstract.adr import AbstractAction, AbstractRequest


def adr(action: AbstractAction=None, request: AbstractRequest=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            valid = request.validate()
            if not valid:
                raise UnprocessableEntity("Invalid request")
            response = action.execute(request)
            return response
        return wrapper
    return decorator

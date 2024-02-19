from functools import wraps

from flask import request as flask_request
from werkzeug.exceptions import UnprocessableEntity

from Dependency import Dependency
from presentation.abstract.adr import AbstractAction, AbstractRequest

di = Dependency()

def adr(ActionClass, RequestClass):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            request: AbstractRequest = RequestClass(flask_request, **kwargs)
            valid = request.validate()
            if not valid:
                raise UnprocessableEntity("Invalid request")
            action: AbstractAction = di.resolve(ActionClass)
            response = action.execute(request)
            return response
        return wrapper
    return decorator

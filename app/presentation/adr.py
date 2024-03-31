from dependency import di
from flask import request as flask_request
from presentation.interface.adr import AdrAction, AdrRequest
from werkzeug.exceptions import UnprocessableEntity


def adr(ActionClass, RequestClass, **kwargs):
    request: AdrRequest = RequestClass(flask_request, **kwargs)
    valid = request.validate()
    if not valid:
        raise UnprocessableEntity("Invalid request")
    action: AdrAction = di.resolve(ActionClass)
    response = action.execute(request)
    return response

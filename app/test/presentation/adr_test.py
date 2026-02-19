from __future__ import annotations

import pytest
from dependency import di
from flask import Response
from presentation.adr import adr
from presentation.route import wsgi
from werkzeug.exceptions import UnprocessableEntity


class DummyAction:
    def __init__(self, response: Response) -> None:
        self.response = response
        self.last_request: DummyRequest | None = None

    def execute(self, request: DummyRequest):
        self.last_request = request
        return self.response


class DummyRequest:
    def __init__(self, request, **kwargs) -> None:
        self.request = request
        self.kwargs = kwargs

    def validate(self) -> bool:
        return True


class InvalidRequest(DummyRequest):
    def validate(self) -> bool:
        return False


class DummyActionClass:
    pass


def test_adr_executes_action_and_returns_response(monkeypatch):
    response = Response("ok", status=200)
    dummy_action = DummyAction(response)

    def fake_resolve(cls):
        assert cls is DummyActionClass
        return dummy_action

    monkeypatch.setattr(di, "resolve", fake_resolve)

    with wsgi.test_request_context("/dummy", method="GET"):
        result = adr(DummyActionClass, DummyRequest, id=123)

    assert result == response
    assert dummy_action.last_request is not None
    assert dummy_action.last_request.kwargs["id"] == 123
    assert dummy_action.last_request.request.path == "/dummy"


def test_adr_raises_on_invalid_request(monkeypatch):
    resolve_called = False

    def fake_resolve(_cls):
        nonlocal resolve_called
        resolve_called = True
        return DummyAction(Response("should-not-be-used"))

    monkeypatch.setattr(di, "resolve", fake_resolve)

    with wsgi.test_request_context("/dummy", method="GET"):  # noqa: SIM117
        with pytest.raises(UnprocessableEntity):
            adr(DummyActionClass, InvalidRequest)

    assert resolve_called is False

from flask import Flask, request

from presentation.api.user import actions, requests
from presentation.decorators.adr import adr

router = Flask(__name__)

@router.route("/")
@adr(action=actions.hello_world.Action(), request=requests.hello_world.Request(request))
def hello_world():
    pass

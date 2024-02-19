from flask import Flask

from presentation.api.user import actions, requests
from presentation.decorators.adr import adr

router = Flask(__name__)

@router.route("/")
@adr(ActionClass=actions.hello_world.Action, RequestClass=requests.hello_world.Request)
def hello_world():
    pass

@router.route("/user/<int:id>")
@adr(ActionClass=actions.get_user.Action, RequestClass=requests.get_user.Request)
def get_user(id):
    pass

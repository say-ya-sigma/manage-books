from flask import Flask
from presentation.adr import adr
from presentation.api.user import actions, requests

wsgi = Flask(__name__)

@wsgi.route("/")
def hello_world():
    return adr(actions.hello_world.Action, requests.hello_world.HelloWorldRequest)

@wsgi.route("/user/<int:id>")
def get_user(id):
    return adr(actions.get_user.Action, requests.get_user.GetUserRequest, id=id)

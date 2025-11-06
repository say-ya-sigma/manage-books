from flask import Flask
from presentation.adr import adr
from presentation.api.book.category import actions as BookCategoryActions
from presentation.api.book.category import requests as BookCategoryRequests
from presentation.api.user import actions as UserActions
from presentation.api.user import requests as UserRequests

wsgi = Flask(__name__)

@wsgi.route("/")
def hello_world():
    return adr(
        UserActions.hello_world.Action,
        UserRequests.hello_world.HelloWorldRequest
    )

@wsgi.route("/user/<int:id>")
def get_user(id):
    return adr(UserActions.get_user.Action, UserRequests.get_user.GetUserRequest, id=id)

@wsgi.route("/book/category/<int:id>")
def get_book_category(id):
    return adr(
        BookCategoryActions.get_category.Action,
        BookCategoryRequests.get_category.GetCategoryRequest,
        id=id
    )

@wsgi.post("/book/category")
def create_book_category():
    return adr(
        BookCategoryActions.create_category.Action,
        BookCategoryRequests.create_category.CreateCategoryRequest,
    )

@wsgi.post("/auth/login")
def login():
    return adr(
        UserActions.login.Action,
        UserRequests.login.LoginRequest
    )

from entity.user.UserId import UserId
from injector import inject
from repository.UserRepository import UserRepository


class UserService:
    @inject
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def get_user(self, user_id: UserId):
        return self.user_repository.find_by_id(user_id)

from entity.user import UserId
from injector import inject
from presentation.api.user.responders import get_user
from repository.UserRepository import AbstractUserRepository


class UserService:
    @inject
    def __init__(self, user_repository: AbstractUserRepository):
        self.__user_repository = user_repository

    def get_user(self, user_id: UserId) -> get_user.GetUserResponseDto:
        user = self.__user_repository.find_by_id(user_id)
        return get_user.GetUserResponseDto(user)

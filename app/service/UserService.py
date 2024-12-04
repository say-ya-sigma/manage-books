from entity.user.UserId import UserId
from injector import inject
from presentation.api.user.responders.get_user import GetUserResponseDto
from repository.UserRepository import UserRepository


class UserService:
    @inject
    def __init__(self, user_repository: UserRepository):
        self._user_repository = user_repository

    def get_user(self, user_id: UserId) -> GetUserResponseDto:
        user = self._user_repository.find_by_id(user_id)
        return GetUserResponseDto(user)

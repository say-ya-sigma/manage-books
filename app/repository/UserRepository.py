from abc import ABC, abstractmethod

from entity.user.UserId import UserId
from error.common import NotFoundException
from orm.models.User import User


class AbstractUserRepository(ABC):
    @abstractmethod
    def find_all(self):
        raise NotImplementedError

    @abstractmethod
    def find_by_id(self, id: UserId):
        raise NotImplementedError


class UserRepository(AbstractUserRepository):
    def find_all(self):
        return map(lambda user: user.to_entity(), User.query.all())

    def find_by_id(self, id: UserId):
        user = User.query.filter(User.id == id.value).first()
        if user is None:
            raise NotFoundException()
        return user.to_entity()

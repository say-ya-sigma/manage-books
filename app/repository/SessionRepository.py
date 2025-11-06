from abc import ABC, abstractmethod

from entity.session import CreateSession as EntityCreateSession
from entity.session import Session as EntitySession
from error.common import NotFoundException
from orm.models.Session import Session


class AbstractSessionRepository(ABC):
    @abstractmethod
    def create_session(self, session: EntityCreateSession):
        raise NotImplementedError

    @abstractmethod
    def find_by_token(self, token: str) -> EntitySession:
        raise NotImplementedError


class SessionRepository(AbstractSessionRepository):
    def create_session(self, session):
        newSession = Session(
            token=session.token,
            user_id=session.user_id.value,
            expired_at=session.expired_at
        )
        newSession.save()

    def find_by_token(self, token: str):
        session = Session.query.filter(Session.token == token).first()
        if session is None:
            raise NotFoundException
        return session.to_entity()

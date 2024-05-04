from orm.seeders.seeders_session import seeders_session
from sqlalchemy.orm import Session

from .users_seeder import users_seeder


def run(session: Session | None = None):
    if session is None:
        session = seeders_session
    users_seeder(session)

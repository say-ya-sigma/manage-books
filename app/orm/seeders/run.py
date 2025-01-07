from orm.seeders.seeders_session import seeders_session
from sqlalchemy.orm import Session

from .book_category_seeder import book_category_seeder
from .users_seeder import users_seeder


def run(session: Session | None = None):
    if session is None:
        session = seeders_session
    users_seeder(session)
    book_category_seeder(session)
    session.close()

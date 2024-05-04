from orm.models.User import User
from sqlalchemy.orm import Session


def users_seeder(session: Session):
    session.bulk_save_objects(
        [
            User(1, "user1", "user1@vantan.jp", "password1"),
            User(2, "user2", "user2@vantan.jp", "password2"),
            User(3, "user3", "user3@vantan.jp", "password3"),
        ]
    )
    session.commit()
    session.close()

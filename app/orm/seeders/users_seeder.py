from orm.models.User import User
from orm.seeders.seeders_session import seeders_session


def users_seeder():
    with seeders_session() as session:
        session.bulk_save_objects(
            [
                User(1, "user1", "user1@vantan.jp", "password1"),
                User(2, "user2", "user2@vantan.jp", "password2"),
                User(3, "user3", "user3@vantan.jp", "password3"),
            ]
        )
        session.commit()
        session.close()

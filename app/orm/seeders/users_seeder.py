from bcrypt import hashpw
from orm.models.User import User
from sqlalchemy.orm import Session


def users_seeder(session: Session):
    session.bulk_save_objects(
        [
            User(
                1,
                "user1",
                "user1@vantan.jp",
                "$2b$12$Xb6gUKMsOYWGabGCq8pXY.tk9Afpzi.xA8RANxitbAW4ISI7c9VGS"
            ), # bcrypt.hashpw(b"password1",bcrypt.gensalt()).decode()
            User(
                2,
                "user2",
                "user2@vantan.jp",
                "$2b$12$20L2qseLQVZfbxhzwiRgQuaB4K069L4zdc.Crfebi8DVTVDwyWoe6"
            ), # bcrypt.hashpw(b"password2",bcrypt.gensalt()).decode()
            User(
                3,
                "user3",
                "user3@vantan.jp",
                "$2b$12$mAB5PmHFbkrzMmw59rX4uuMhCPJu25/Fhkg1pTYQgnlfdWE1E4ydG"
            ), # bcrypt.hashpw(b"password2",bcrypt.gensalt()).decode()
        ]
    )
    session.commit()

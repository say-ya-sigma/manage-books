from orm.models.BookCategory import BookCategory
from sqlalchemy.orm import Session


def book_category_seeder(session: Session):
    session.bulk_save_objects(
        [
            BookCategory("category1"),
            BookCategory("category2")
        ]
    )
    session.commit()

from orm.models.BookCategory import BookCategory
from sqlalchemy.orm import Session


def book_category_seeder(session: Session, minimal: bool = False):
    categories = [BookCategory("category1")]
    if not minimal:
        categories.extend(
            [
                BookCategory("category2"),
                BookCategory("category3"),
            ]
        )
    session.bulk_save_objects(categories)
    session.commit()

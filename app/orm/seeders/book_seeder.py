from orm.models.Book import Book
from sqlalchemy.orm import Session


def book_seeder(session: Session):
    session.bulk_save_objects(
        [
            Book(
                title="たのしいPython",
                author="VANTAN",
                isbn="1111111111111",
                publisher="VANTAN",
                book_category_id=1,
            ),
        ]
    )
    session.commit()

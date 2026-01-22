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
            Book(
                title="たのしいJava",
                author="Author A",
                isbn="2222222222222",
                publisher="Pub A",
                book_category_id=2,
            ),
            Book(
                title="たのしいC",
                author="Author B",
                isbn="3333333333333",
                publisher="Pub B",
                book_category_id=3,
            ),
            Book(
                title="たのしいGo",
                author="Author C",
                isbn="4444444444444",
                publisher="Pub C",
                book_category_id=1,
            ),
            Book(
                title="たのしいRust",
                author="Author D",
                isbn="5555555555555",
                publisher="Pub D",
                book_category_id=2,
            ),
            Book(
                title="たのしいRuby",
                author="Author E",
                isbn="6666666666666",
                publisher="Pub E",
                book_category_id=3,
            ),
            Book(
                title="たのしいJavaScript",
                author="Author F",
                isbn="7777777777777",
                publisher="Pub F",
                book_category_id=1,
            ),
            Book(
                title="たのしいTypeScript",
                author="Author G",
                isbn="8888888888888",
                publisher="Pub G",
                book_category_id=2,
            ),
            Book(
                title="たのしいSQL",
                author="Author H",
                isbn="9999999999999",
                publisher="Pub H",
                book_category_id=3,
            ),
            Book(
                title="たのしいAlgorithms",
                author="Author I",
                isbn="1234567890123",
                publisher="Pub I",
                book_category_id=1,
            ),
            Book(
                title="たのしいDataScience",
                author="Author J",
                isbn="9876543210987",
                publisher="Pub J",
                book_category_id=2,
            ),
        ]
    )
    session.commit()

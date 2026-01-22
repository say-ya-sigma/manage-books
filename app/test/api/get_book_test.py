from flask.testing import FlaskClient


def test_get_book(client: FlaskClient):
    response = client.get("/book/1")

    assert response.status_code == 200

    json_data = response.get_json()

    expected_data = {
        "id": 1,
        "title": "たのしいPython",
        "author": "VANTAN",
        "isbn": "1111111111111",
        "publisher": "VANTAN",
        "book_category_id": 1,
        "book_category_name": "category1",
    }

    assert json_data == expected_data

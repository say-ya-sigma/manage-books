from flask.testing import FlaskClient


def test_update_category(client: FlaskClient):
    # エンドポイントにリクエストを送信
    response = client.put("/book/category", json={
        "book_category_id": 1,
        "name": "category-test"
    })

    # レスポンスのステータスコードが200 (OK) であることを確認
    assert response.status_code == 200

from flask.testing import FlaskClient


def test_update_category(client: FlaskClient):
    # エンドポイントにリクエストを送信
    response = client.delete("/book/category", json={
        "book_category_id": 1
    })

    # レスポンスのステータスコードが200 (OK) であることを確認
    assert response.status_code == 200

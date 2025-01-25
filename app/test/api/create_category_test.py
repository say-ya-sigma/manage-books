from flask.testing import FlaskClient


def test_create_category(client: FlaskClient):
    # エンドポイントにリクエストを送信
    response = client.post("/book/category", json={
        "name": "category-test"
    })

    # レスポンスのステータスコードが200 (OK) であることを確認
    assert response.status_code == 200

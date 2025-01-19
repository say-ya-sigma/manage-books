from flask.testing import FlaskClient


def test_get_category(client: FlaskClient):
    # エンドポイントにリクエストを送信
    response = client.get("/book/category/1")

    # レスポンスのステータスコードが200 (OK) であることを確認
    assert response.status_code == 200

    # レスポンスのJSONデータを取得
    json_data = response.get_json()

    # 期待するJSONデータ
    expected_data = {
        "id": 1,
        "name": "category1",
    }

    # 実際のJSONデータと期待するJSONデータが一致することを確認
    assert json_data == expected_data

from flask.testing import FlaskClient


def test_login(client: FlaskClient):
    # エンドポイントにリクエストを送信
    response = client.post("/auth/login", json={
        "email": "user1@vantan.jp",
        "password": "password1"
    })

    # レスポンスのステータスコードが200 (OK) であることを確認
    assert response.status_code == 200

    # レスポンスのJSONデータを取得
    json_data = response.get_json()

    assert "token" in json_data
    assert "expired_at" in json_data
    assert isinstance(json_data["token"], str)
    assert len(json_data["token"]) == 64
    assert isinstance(json_data["expired_at"], str)


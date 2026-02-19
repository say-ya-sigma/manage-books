from datetime import datetime, timedelta

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

    expired_at = datetime.fromisoformat(json_data["expired_at"])
    now = datetime.now()
    assert expired_at >= now
    assert expired_at <= now + timedelta(days=31)


def test_login_missing_body_returns_422(client: FlaskClient):
    response = client.post("/auth/login")

    assert response.status_code == 422


def test_login_missing_email_returns_422(client: FlaskClient):
    response = client.post("/auth/login", json={
        "password": "password1"
    })

    assert response.status_code == 422


def test_login_missing_password_returns_422(client: FlaskClient):
    response = client.post("/auth/login", json={
        "email": "user1@vantan.jp"
    })

    assert response.status_code == 422


def test_login_wrong_password_returns_500(client: FlaskClient):
    response = client.post("/auth/login", json={
        "email": "user1@vantan.jp",
        "password": "invalid_password"
    })

    assert response.status_code == 500


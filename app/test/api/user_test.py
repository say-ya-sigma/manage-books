def test_endpoint_response(client):
    # エンドポイントにリクエストを送信
    response = client.get("/user/1")

    # レスポンスのステータスコードが200 (OK) であることを確認
    assert response.status_code == 200

    # レスポンスのJSONデータを取得
    json_data = response.get_json()

    # 期待するJSONデータ
    expected_data = {
        "id": 1,
        "name": "user1",
        "email": "user1@vantan.jp"
    }

    # 実際のJSONデータと期待するJSONデータが一致することを確認
    assert json_data == expected_data

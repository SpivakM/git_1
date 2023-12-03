import jwt_tokens


def test_normal_jwt():
    payload = jwt_tokens.PAYLOAD
    data = jwt_tokens.encode_jwt(payload)
    result = jwt_tokens.decode_jwt(data)
    assert result == payload


def test_expired_jwt():
    payload = jwt_tokens.PAYLOAD
    payload["exp"] = 0
    data = jwt_tokens.encode_jwt(payload)
    result = jwt_tokens.decode_jwt(data)
    assert result == {}

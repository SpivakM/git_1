import jwt

import settings

PAYLOAD = {
    "my_name": "Matvii",
    "age": 15,
    "exp": 1705783872,
}


def encode_jwt(payload: dict) -> str:
    return jwt.encode(
        payload=payload,
        key=settings.JWT_SECRET,
        algorithm="HS256",
    )


data = encode_jwt(PAYLOAD)


def decode_jwt(encoded_jwt: str) -> dict:
    try:
        return jwt.decode(
            encoded_jwt,
            key=settings.JWT_SECRET,
            algorithms=["HS256"],
        )
    except jwt.ExpiredSignatureError:
        return {}
    except jwt.InvalidSignatureError:
        return {}

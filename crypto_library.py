import hashlib

from passlib.context import CryptContext

context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# ------------- passlib -----------------------------------
def get_password_hash(value: str) -> str:
    hash1 = context.hash(value)
    return hash1


def verify_password(plain_password: str, saved_password_hash: str) -> bool:
    result = context.verify(plain_password, saved_password_hash)
    return result


# -------------- md5 --------------------------------------


def encode_md5(value: str) -> str:
    hash1 = hashlib.md5(value.encode()).hexdigest()
    return hash1


# ---------------------------------------------------------

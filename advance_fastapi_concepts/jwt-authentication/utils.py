from passlib.context import CryptContext

# Use Argon2 instead of bcrypt
pwd_context = CryptContext(schemes=['argon2'], deprecated='auto')

fake_user_db = {
    'johndoe': {
        'username': 'johndoe',
        'hashed_password': pwd_context.hash('secret123')
    }
}


def get_user(username: str):
    user = fake_user_db.get(username)
    return user


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

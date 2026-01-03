from app.services.auth import pwd_context, fake_users_db


def test_password_hashing_and_verify():
    password = "StrongPass!234"
    hashed = pwd_context.hash(password)
    assert hashed != password
    assert pwd_context.verify(password, hashed)


def test_fake_users_db_structure():
    # fake_users_db should be a dict-like mapping with username keys
    assert isinstance(fake_users_db, dict)

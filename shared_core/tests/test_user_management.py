import uuid

from app.services.user_management import (
    list_users,
    create_user,
    update_user_role,
    delete_user,
)
from app.services.auth import fake_users_db


def test_create_update_delete_user():
    # unique username to avoid collisions
    username = f"testuser_{uuid.uuid4().hex[:8]}"
    password = "TestPass123!"
    role = "analyst"

    # create
    created = create_user(username=username, password=password, role=role, actor="test-runner")
    assert created is not None
    assert created["username"] == username
    assert created["role"] == role

    # list users contains the new user
    users = list_users()
    assert any(u["username"] == username for u in users)

    # update role
    new_role = "admin"
    updated = update_user_role(username=username, new_role=new_role, actor="test-runner")
    assert updated is not None
    assert updated["role"] == new_role

    # delete
    result = delete_user(username=username, actor="test-runner")
    assert result is True
    assert username not in fake_users_db

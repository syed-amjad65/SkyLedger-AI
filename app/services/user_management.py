from app.services.auth import fake_users_db, pwd_context
from app.services.audit_logs import log_event


def list_users():
    # We only expose username + role, not password
    return [
        {"username": u["username"], "role": u["role"]}
        for u in fake_users_db.values()
    ]


def create_user(username: str, password: str, role: str, actor: str = "superadmin"):
    if username in fake_users_db:
        return None  # user already exists

    fake_users_db[username] = {
        "username": username,
        "hashed_password": pwd_context.hash(password),
        "role": role,
    }

    # ✅ Log the creation event
    log_event(actor, "create_user", {"username": username, "role": role})

    return {"username": username, "role": role}


def update_user_role(username: str, new_role: str, actor: str = "superadmin"):
    user = fake_users_db.get(username)
    if not user:
        return None

    old_role = user["role"]
    user["role"] = new_role

    # ✅ Log the role change
    log_event(actor, "update_role", {"username": username, "old_role": old_role, "new_role": new_role})

    return {"username": username, "role": new_role}


def delete_user(username: str, actor: str = "superadmin"):
    if username not in fake_users_db:
        return None

    # ✅ Log before deletion
    log_event(actor, "delete_user", {"username": username, "role": fake_users_db[username]["role"]})

    del fake_users_db[username]
    return True
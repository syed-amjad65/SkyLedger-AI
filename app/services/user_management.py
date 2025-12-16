from app.services.auth import fake_users_db, pwd_context

def list_users():
    return [
        {"username": u["username"], "role": u["role"]}
        for u in fake_users_db.values()
    ]


def create_user(username: str, password: str, role: str):
    if username in fake_users_db:
        return None  # user already exists

    fake_users_db[username] = {
        "username": username,
        "hashed_password": pwd_context.hash(password),
        "role": role,
    }
    return {"username": username, "role": role}


def update_user_role(username: str, new_role: str):
    user = fake_users_db.get(username)
    if not user:
        return None

    user["role"] = new_role
    return {"username": username, "role": new_role}


def delete_user(username: str):
    if username not in fake_users_db:
        return None

    del fake_users_db[username]
    return True
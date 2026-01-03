from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError

# ✅ Shared JWT settings (MUST match auth.py)
SECRET_KEY = "skyledger_super_secret_2025"
ALGORITHM = "HS256"

# ✅ HTTP Bearer auth for Swagger and requests
oauth2_scheme = HTTPBearer()


def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(oauth2_scheme)):
    """
    Extract and validate JWT from Authorization: Bearer <token>.
    """
    token = credentials.credentials

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str | None = payload.get("sub")
        role: str | None = payload.get("role")

        if username is None or role is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token payload",
            )

        return {"username": username, "role": role}

    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
        )


def require_any_role(allowed_roles: list[str]):
    """
    Generic RBAC: allow any of the given roles.
    """

    def role_checker(user=Depends(get_current_user)):
        if user["role"] not in allowed_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You do not have permission to access this resource",
            )
        return user

    return role_checker


def require_role(role: str):
    """
    Backward-compatible single-role helper.
    """
    return require_any_role([role])


def require_superadmin():
    """
    Superadmin-only helper.
    """
    return require_any_role(["superadmin"])

from pydantic import BaseModel

class CreateUserRequest(BaseModel):
    username: str
    password: str
    role: str


class UpdateRoleRequest(BaseModel):
    role: str


class UserResponse(BaseModel):
    username: str
    role: str
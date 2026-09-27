from uuid import UUID

from pydantic import BaseModel, ConfigDict, EmailStr


class UserRequest(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    uuid: UUID
    first_name: str
    last_name: str

    model_config = ConfigDict(
        from_attributes=True,
    )


class UserUpdateRequest(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr


class UserUpdatePasswordRequest(BaseModel):
    password: str

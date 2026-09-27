from uuid import UUID

from fastapi import APIRouter

from src.models.schemas import (
    UserRequest,
    UserResponse,
    UserUpdatePasswordRequest,
    UserUpdateRequest,
)

router = APIRouter(tags=["User"], prefix="/user")


@router.post("/create", response_model=UserResponse)
async def create(payload: UserRequest) -> UserResponse: ...


@router.get("/me", response_model=UserResponse)
async def get_current_user() -> UserResponse: ...


@router.put("/update/{uuid}")
async def update(
    uuid: UUID, payload: UserUpdateRequest | UserUpdatePasswordRequest
) -> bool: ...


@router.delete("/delete/{uuid}")
async def delete(uuid: UUID) -> bool: ...

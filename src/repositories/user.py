from src.models.entities import UserModel
from src.models.schemas import UserRequest, UserUpdateRequest
from src.repositories.base import CRUDRepository


class UserRepository(
    CRUDRepository[UserModel, UserRequest, UserUpdateRequest],
):
    entity = UserModel

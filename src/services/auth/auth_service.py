from typing import List
from uuid import UUID

from src.models.auth.models import User
from src.repositories.auth.auth_repository import AuthRepository
from src.schemas.pydantic.auth_schema import UserBase, UserDTO


class AuthService:
    def __init__(self, repo: AuthRepository):
        self._repo = repo

    def get_user_by_id(self, uuid: str) -> UserDTO:
        user = self._repo.get(uuid=uuid)
        return UserDTO(uuid=user.uuid,
                       username=user.username,
                       email=user.email)

    def create_new_user(self, user: UserBase) -> UserDTO:
        created_user = self._repo.add(user)
        return UserDTO(uuid=created_user.uuid,
                       username=created_user.username,
                       email=created_user.email)

    def delete_user(self, uuid: UUID) -> None:
        return self._repo.delete(uuid)

    def get_all_users(self, start_index: int, page_size: int) -> List[UserDTO]:
        return [UserDTO(uuid=user.uuid,
                        username=user.username,
                        email=user.email) for user in self._repo.list(start_index, page_size)]

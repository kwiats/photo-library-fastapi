from src.repositories.auth.auth_repository import AuthRepository
from src.schemas.pydantic.auth_schema import UserBase, UserDTO


class AuthUOW:
    def __init__(self, repo: AuthRepository):
        self._repo = repo

    def get_user_id(self, user_id: int) -> UserDTO:
        return self._repo.get(user_id)

    def create_user(self, user_data: UserBase) -> UserDTO:
        return self._repo.add(user_data)

    # def get_user_username(self, username: str) -> Type[User]:
    #     return self._repo.get_user_by_username(username)
    #
    # def get_all_users(self, pageSize: Optional[int] = 10, startIndex: Optional[int] = 0) -> list[User]:
    #     return [user for user in self._repo.get_users(pageSize, startIndex) if not user.is_deleted]
    #
    # def get_active_users(self) -> list[User]:
    #     return [user for user in self._repo.get_users() if not user.is_deleted and user.is_active]



    # def delete_user(self, obj: UserValueObject, force_delete: bool) -> None:
    #     if force_delete:
    #         return self._repo.delete_user(obj)
    #     return self.change_user_parameters(obj, 'is_deleted', True)
    #
    # def change_user_parameters(self, obj: UserValueObject, param: str, value: Union[str, int, bool, list[str]]) -> None:
    #     if not hasattr(obj, param):
    #         raise ValueError(f'User has not {param} parameter')
    #     return self._repo.change_obj_param(obj, param, value)
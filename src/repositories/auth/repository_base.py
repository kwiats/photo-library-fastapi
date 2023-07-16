import abc
from typing import List, Optional, Union, Type
from uuid import UUID

from src.schemas.pydantic.auth_schema import UserCreate, UserDTO


class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def add(self, user: UserCreate):
        raise NotImplementedError

    @abc.abstractmethod
    def delete(self, uuid: UUID):
        raise NotImplementedError

    @abc.abstractmethod
    def update(self, user: UserDTO, key: str, value: Union[str, int]):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, uuid: str) -> UserDTO:
        raise NotImplementedError

    @abc.abstractmethod
    def list(self, limit: Optional[int], start: Optional[int]) -> List[UserDTO]:
        raise NotImplementedError

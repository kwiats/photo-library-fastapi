from typing import List, Union
from uuid import UUID

from fastapi import Depends
from sqlalchemy.orm import Session

from src.configs.database import get_db_connection
from src.models.auth.models import User
from src.repositories.auth.repository_base import AbstractRepository
from src.schemas.pydantic.auth_schema import UserCreate, UserDTO


class AuthRepository(AbstractRepository):
    def __init__(self, session: Session = Depends(get_db_connection)):
        self._session = session

    def delete(self, uuid: UUID):
        user_obj = self._session.query(User).filter_by(uuid=uuid).first()
        if user_obj:
            with self._session.begin():
                self._session.delete(user_obj)

    def update(self, user: UserDTO, key: str, value: Union[str, int]) -> User:
        user_obj = self._session.query(User).filter_by(uuid=user.uuid).first()
        if not user_obj:
            raise ValueError(f'User about index {user.uuid} doesnt exists')
        with self._session.begin():
            setattr(user_obj, key, value)
            self._session.refresh(user_obj)
        return user_obj

    def get(self, uuid: str) -> User:
        user = self._session\
            .query(User)\
            .filter_by(uuid=uuid)\
            .first()

        return user

    def list(self, start: int,
             limit: int) -> List[User]:
        users = self._session.query(User).offset(start).limit(limit).all()
        return users

    def add(self, user: UserCreate) -> User:
        created_user = User(**user.model_dump())
        self._session.add(created_user)
        self._session.commit()
        self._session.refresh(created_user)
        return created_user

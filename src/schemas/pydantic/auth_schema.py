from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class UserBase(BaseModel):
    pass


class UserCreate(UserBase):
    username: str
    password: str
    email: str


class UserDTO(UserBase):
    uuid: UUID
    username: str
    email: str

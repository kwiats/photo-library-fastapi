from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class UserBase(BaseModel):
    uuid: UUID
    username: str
    password: str
    email: str
    is_active: bool
    created_date: datetime


class UserDTO(BaseModel):
    uuid: UUID
    username: str
    email: str

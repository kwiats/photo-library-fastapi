from datetime import datetime
from uuid import UUID

import pytest
from pydantic import ValidationError

from src.models.auth.models import User
from src.schemas.pydantic.auth_schema import UserBase, UserDTO


def test_userbase_creation():
    uuid = "123e4567-e89b-12d3-a456-426614174000"
    username = "john_doe"
    password = "password123"
    email = "john@example.com"
    is_active = True
    created_date = datetime.now()

    user = UserBase(
        uuid=uuid,
        username=username,
        password=password,
        email=email,
        is_active=is_active,
        created_date=created_date
    )

    assert user.uuid == UUID(uuid)
    assert user.username == username
    assert user.password == password
    assert user.email == email
    assert user.is_active == is_active
    assert user.created_date == created_date


def test_userbase_missing_required_fields():
    with pytest.raises(ValidationError):
        user = UserBase(
            uuid="123e4567-e89b-12d3-a456-426614174000",
            username="john_doe",
            password="password123",
            email="john@example.com",
            is_active=True
        )


def test_userbase_invalid_field_types():
    with pytest.raises(ValidationError):
        user = UserBase(
            uuid="123e4567-e89b-12d3-a456-426614174000",
            username="john_doe",
            password="password123",
            email="john@example.com",
            is_active="true",
            datetime=datetime.now().isoformat()
        )


def test_user_to_userDTO():
    uuid = UUID("123e4567-e89b-12d3-a456-426614174000")
    username = "john_doe"
    email = "john@example.com"

    user = User(
        uuid=uuid,
        username=username,
        email=email
    )

    userDTO = UserDTO(
        uuid=user.uuid,
        username=user.username,
        email=user.email
    )

    assert user.uuid == userDTO.uuid
    assert user.username == userDTO.username
    assert user.email == userDTO.email

def test_userbase_to_userDTO():
    uuid = "123e4567-e89b-12d3-a456-426614174000"
    username = "john_doe"
    password = "password123"
    email = "john@example.com"
    is_active = True
    created_date = datetime.now()

    user = UserBase(
        uuid=uuid,
        username=username,
        password=password,
        email=email,
        is_active=is_active,
        created_date=created_date
    )

    userDTO = UserDTO(**user.model_dump())

    assert user.uuid == userDTO.uuid
    assert user.username == userDTO.username
    assert user.email == userDTO.email

from datetime import datetime
from unittest.mock import Mock

from src.repositories.auth.auth_repository import AuthRepository
from src.schemas.pydantic.auth_schema import UserBase
from src.services.auth.auth_service import AuthService


def test_get_user_by_id():
    uuid = "123e4567-e89b-12d3-a456-426614174000"
    username = "john_doe"
    password = "password123"
    email = "john@example.com"
    is_active = True
    user = UserBase(
        uuid=uuid,
        username=username,
        password=password,
        email=email,
        is_active=is_active,
        created_date=datetime.now()
    )

    mock_uow = Mock(spec=AuthRepository)
    mock_uow.get.return_value = user
    auth_service = AuthService(repo=mock_uow)
    result = auth_service.get_user_by_id(uuid=uuid)
    mock_uow.get_user_id.assert_called_once_with(uuid=uuid)

    assert result == user

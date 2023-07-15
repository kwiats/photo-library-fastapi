from typing import List, Optional

from fastapi import APIRouter, Depends

from src.repositories.auth.auth_repository import AuthRepository
from src.schemas.pydantic.auth_schema import UserDTO, UserBase
from src.services.auth.auth_service import AuthService

AuthRouter = APIRouter(
    prefix="/authorization", tags=['authorization']
)


@AuthRouter.get("/user/", response_model=UserDTO)
def get_all_users(user: UserBase,
                  authService: AuthService = Depends()
                  ) -> UserDTO:
    return authService.create_new_user(user)

# @AuthRouter.get("/user/{uuid}", response_model=UserDTO)
# def get_all_users(uuid: str,
#                   authService: AuthService = Depends()
#                   ):
#     return authService.get(uuid)

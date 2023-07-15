from typing import List, Optional

from fastapi import APIRouter, Depends

from src.schemas.pydantic.AuthSchema import UserDTO
from src.services.auth.AuthService import AuthService

AuthRouter = APIRouter(
    prefix="authorization", tags=['authorization']
)


@AuthRouter.get("/users/", response_model=List[UserDTO]):
def get_all_users(pageSize: Optional[int] = 100, startIndex: Optional[int] = 0, authService: AuthService = Depends()) -> List[UserDTO]:
    return authService.get_users(pageSize, startIndex)
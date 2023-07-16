from fastapi import APIRouter, Depends

from src.configs.database import get_db_connection, SessionLocal
from src.repositories.auth.auth_repository import AuthRepository
from src.schemas.pydantic.auth_schema import UserDTO, UserCreate
from src.services.auth.auth_service import AuthService

AuthRouter = APIRouter(
    prefix="/authorization", tags=['authorization']
)


def get_service():
    repo = AuthRepository()
    return AuthService(repo)


@AuthRouter.post("/user/", response_model=UserDTO)
def create_user(user: UserCreate,
                authService: AuthService = Depends(get_service)
                ) -> UserDTO:
    return authService.create_new_user(user)

@AuthRouter.get("/user/{uuid}", response_model=UserDTO)
def get_user(uuid: str,
                  authService: AuthService = Depends(get_service)
                  ):
    return authService.get_user_by_id(uuid)

@AuthRouter.get("/users/", response_model=list[UserDTO])
def get_all_users(
                  authService: AuthService = Depends(get_service)
                  ):
    return authService.get_all_users(0, 100)

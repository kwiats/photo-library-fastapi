from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_DAYS: int = 31
    DATABASE_URL: str
    DEBUG_MODE: bool


def get_environment_variables():
    return Settings()

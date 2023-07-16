from datetime import datetime
from uuid import uuid4

from sqlalchemy import create_engine, MetaData, Table, Column, Uuid, String, Boolean, DateTime
from sqlalchemy.orm import DeclarativeBase, sessionmaker, scoped_session

from src.configs.settings import get_environment_variables

env = get_environment_variables()

engine = create_engine(env.DATABASE_URL, echo=env.DEBUG_MODE)

metadata_obj = MetaData()

SessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine
)

user_table = Table('user',
                   metadata_obj,
                   Column('uuid', Uuid, primary_key=True, default=uuid4),
                   Column('username', String(30), nullable=False, unique=True),
                   Column('password', String, nullable=False),
                   Column('email', String),
                   Column('is_active', Boolean, default=False),
                   Column('created_date', DateTime, default=datetime.now),
                   )


class Base(DeclarativeBase):
    pass


def init():
    metadata_obj.create_all(engine)
    Base.metadata.create_all(engine)


def get_db_connection():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

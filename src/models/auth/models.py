from datetime import datetime
from uuid import UUID, uuid4


from sqlalchemy import String, Boolean, DateTime
from sqlalchemy.orm import mapped_column, Mapped

from src.configs.database import Base


class User(Base):
    __tablename__ = 'user'

    uuid: Mapped[UUID] = mapped_column(String(30), primary_key=True, default=uuid4())
    username: Mapped[str] = mapped_column(String(30))
    password: Mapped[str]
    email: Mapped[str]
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    created_date: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())

    def __repr__(self):
        return f"User(uuid={self.uuid!r}, username={self.username!r}, is_active={self.is_active!r})"
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src.models.entities import BaseModel


class UserModel(BaseModel):
    __tablename__ = "users"
    first_name: Mapped[str] = mapped_column(String(10), nullable=False)
    last_name: Mapped[str] = mapped_column(String(60), nullable=False)
    email: Mapped[str] = mapped_column(String(120), nullable=False)
    password: Mapped[str] = mapped_column(String(60), nullable=False)

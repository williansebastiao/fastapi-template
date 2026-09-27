import uuid
from typing import ClassVar

import pendulum
from sqlalchemy import DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from src.core import settings

Base = DeclarativeBase


class BaseModel(Base):
    __abstract__ = True
    __table_args__: ClassVar[dict[str, str]] = {
        "schema": settings.DATABASE_SCHEMA
    }

    uuid: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        default=lambda: str(uuid.uuid4()),
        primary_key=True,
        index=True,
    )
    created_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True), default=pendulum.now(), nullable=False
    )
    updated_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        default=pendulum.now(),
        onupdate=pendulum.now(),
        nullable=False,
    )

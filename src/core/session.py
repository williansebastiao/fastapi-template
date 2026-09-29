from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from src.core import settings
from src.exceptions import IntegrityException

engine = create_async_engine(
    settings.database_url,
    future=True,
    echo=False,
    connect_args={
        "server_settings": {"search_path": settings.DATABASE_SCHEMA}
    },
)

AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


async def session():
    async with AsyncSessionLocal() as session:
        try:
            yield session
        except IntegrityError as e:
            await session.rollback()
            raise IntegrityException() from e
        except Exception as e:
            await session.rollback()
            raise e

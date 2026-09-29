from collections.abc import Sequence
from typing import Any
from uuid import UUID

from pydantic import BaseModel
from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.models.entities import BaseModel as EntityModel
from src.models.schemas import PageResponse


class BaseRepository[Entity: EntityModel]:
    entity: type[Entity]

    def __init__(self, session: AsyncSession):
        self.session = session


class CreateRepository[Entity: EntityModel, CreateSchema: BaseModel](
    BaseRepository[Entity]
):
    async def create(self, payload: CreateSchema) -> Entity:
        instance = self.entity(**payload.model_dump())
        self.session.add(instance)
        await self.session.flush()
        await self.session.refresh(instance)
        return instance


class GetAllRepository[Entity: EntityModel](BaseRepository[Entity]):
    async def get_all(self, **filters: Any) -> Sequence[Entity]:
        stmt = select(self.entity).filter_by(**filters)
        return (await self.session.execute(stmt)).scalars().all()


class GetByUuidRepository[Entity: EntityModel](BaseRepository[Entity]):
    async def get_by_uuid(self, uuid: UUID) -> Entity | None:
        return await self.session.get(self.entity, uuid)


class UpdateRepository[Entity: EntityModel, UpdateSchema: BaseModel](
    GetByUuidRepository[Entity]
):
    async def update(self, uuid: UUID, payload: UpdateSchema) -> Entity | None:
        instance = await self.get_by_uuid(uuid)
        if instance is None:
            return None
        for field, value in payload.model_dump(exclude_unset=True).items():
            setattr(instance, field, value)
        await self.session.flush()
        await self.session.refresh(instance)
        return instance


class DeleteRepository[Entity: EntityModel](GetByUuidRepository[Entity]):
    async def delete(self, uuid: UUID) -> bool:
        instance = await self.get_by_uuid(uuid)
        if instance is None:
            return False
        await self.session.delete(instance)
        await self.session.flush()
        return True


class PaginateRepository[Entity: EntityModel](BaseRepository[Entity]):
    async def paginate(
        self, page: int = 1, size: int = 20, **filters: Any
    ) -> PageResponse[Entity]:
        stmt = select(self.entity).filter_by(**filters)

        count_stmt = select(func.count()).select_from(stmt.subquery())
        total = (await self.session.execute(count_stmt)).scalar_one()

        stmt = (
            stmt.order_by(self.entity.created_at.desc(), self.entity.uuid)
            .offset((page - 1) * size)
            .limit(size)
        )
        items = (await self.session.execute(stmt)).scalars().all()
        return PageResponse(
            items=list(items), total=total, page=page, size=size
        )


class CRUDRepository[
    Entity: EntityModel,
    CreateSchema: BaseModel,
    UpdateSchema: BaseModel,
](
    CreateRepository[Entity, CreateSchema],
    GetAllRepository[Entity],
    UpdateRepository[Entity, UpdateSchema],
    DeleteRepository[Entity],
    PaginateRepository[Entity],
):
    pass

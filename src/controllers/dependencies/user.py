from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.controllers.interfaces import ICategoryController
from src.views.dependencies import session as get_session

from src.controllers import CategoryController
from src.repositories import CategoryRepository


def user_dependecy(
    session: Annotated[AsyncSession, Depends(get_session)],
) -> ICategoryController:
    repository = CategoryRepository(session=session)
    return CategoryController(repository=repository)


UserDependecy = Annotated[
    ICategoryController, Depends(get_category_controller)
]

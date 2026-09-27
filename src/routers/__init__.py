from fastapi import APIRouter

from . import (
    autenticate,
    health,
    user,
)

router = APIRouter()

router.include_router(health.router)
router.include_router(autenticate.router)
router.include_router(user.router)

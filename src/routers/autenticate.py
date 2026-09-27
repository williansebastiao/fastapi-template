from fastapi import APIRouter

router = APIRouter(tags=["Autenticate"], prefix="/autenticate")


@router.post("")
async def autenticate(payload: dict): ...

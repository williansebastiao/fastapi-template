from fastapi import APIRouter, Response

from src.core import logger, settings
from src.models.schemas import HealthCheckResponse

router = APIRouter()


@router.get(
    "/health",
    tags=["Health"],
    response_model=HealthCheckResponse,
)
async def health(response: Response) -> HealthCheckResponse:
    logger.info(f"response: {response}")
    return HealthCheckResponse(
        status="OK",
        version=settings.APP_VERSION,
    )

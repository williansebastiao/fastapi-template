from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBearer

from src.core import logger, settings
from src.exceptions import HttpExceptionBase
from src.routers import router
from src.routers.exceptions import global_exception

security = HTTPBearer()


@asynccontextmanager
async def lifespan(_: FastAPI):
    logger.info("Lifespan ok")
    yield


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    docs_url=f"{settings.APP_PATH}/docs",
    redoc_url=f"{settings.APP_PATH}/redoc",
    openapi_url=f"{settings.APP_PATH}/openapi.json",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix=settings.APP_PATH)
app.add_exception_handler(Exception, global_exception)
app.add_exception_handler(HTTPException, global_exception)
app.add_exception_handler(RequestValidationError, global_exception)
app.add_exception_handler(HttpExceptionBase, global_exception)

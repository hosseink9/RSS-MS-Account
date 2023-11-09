from fastapi import FastAPI
import logging
from .api.api_v1.endpoints.routers import router as account_router
from app.log.logging_lib import RouterLoggingMiddleware
from app.core.config import logging_config

logging.config.dictConfig(logging_config)

app = FastAPI()
app.add_middleware(RouterLoggingMiddleware,
                   logger=logging.getLogger("elastic-logger"))
app.include_router(router=account_router, prefix="")

from fastapi import FastAPI
from .api.api_v1.endpoints.routers import router as account_router

app = FastAPI()
app.include_router(router=account_router, prefix="")

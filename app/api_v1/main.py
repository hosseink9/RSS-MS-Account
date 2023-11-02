from fastapi import FastAPI
from endpoints.routers import router as account_routers

app = FastAPI()
app.include_router(router=account_routers, prefix="")

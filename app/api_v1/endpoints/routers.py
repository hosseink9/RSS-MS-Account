from fastapi.routing import APIRouter
from fastapi import Depends, HTTPException, status
from ...schema.schemas import UserRequest
from ...schema.schemas import UserResponse
from ...services.services import UserService, get_user_service
import json

router = APIRouter(tags=["account"])


@router.post("/signup", summary="Create new user", status_code=status.HTTP_201_CREATED, response_model=UserResponse)
async def create_user(data: UserRequest, user_service: UserService = Depends(get_user_service)):
    user = await user_service.create_user(data)
    return user


@router.post("/login", summary="Login user", status_code=status.HTTP_202_ACCEPTED, response_model=UserResponse)
async def login(data: UserRequest, user_service: UserService = Depends(get_user_service)):
    user = await user_service.get_user(data.username, data.password)
    user["id"] = str(user["_id"])
    print(user)
    return user

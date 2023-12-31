from fastapi import Depends, HTTPException, status
from passlib.context import CryptContext
from ..schema.schemas import UserRequest
from motor.motor_asyncio import AsyncIOMotorClient as Client
from ..schema.schemas import UserResponse


def sess_collection():
    db = Client().get_database("rss-feed")
    account_collection = db["users"]
    yield account_collection
    # db.close()


def get_user_service(collection=Depends(sess_collection)):
    return UserService(collection)


class UserService:
    password_context = CryptContext(schemes=['bcrypt'], deprecated="auto")

    def __init__(self, collection):
        self.collection = collection

    def get_hashed_password(self, password: str) -> str:
        return self.password_context.hash(password)

    def verify_password(self, password: str, hashed_pass: str) -> bool:
        return self.password_context.verify(password, hashed_pass)

    async def get_user(self, username: str, password: str):
        user_dict = await self.collection.find_one({'username': username})
        if user_dict is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="User was not found")

        result = self.verify_password(password, user_dict["password"])
        if not result:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Password")

        # return UserRequest(**user_dict)
        return user_dict

    async def authenticate(self, username, password):
        user = await self.get_user(username, password)
        return user

    async def create_user(self, user):
        check_user = await self.collection.find_one({"username": user.username})
        if check_user is not None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="User with this username already exist"
            )
        hashed_password = self.get_hashed_password(user.password)
        data = {"username": user.username, "password": hashed_password,
                "firstname": user.firstname, "lastname": user.lastname}
        await self.collection.insert_one(data)
        # return UserResponse(**data)
        return data

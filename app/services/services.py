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


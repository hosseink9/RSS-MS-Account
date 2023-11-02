# from pymongo import MongoClient
import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017/")
print('🚀 Connected to MongoDB...')

db = client["rss-feed"]
account_collection = db["users"]
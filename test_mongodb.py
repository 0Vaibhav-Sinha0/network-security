# Tests MongoDB connectivity using a ping command to verify the database connection.

import os
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

load_dotenv()

uri = os.getenv("MONGO_DB_URL")

client = MongoClient(uri, server_api=ServerApi('1'))

try:
    client.admin.command('ping')
    print("MongoDB connection successful")
except Exception as e:
    print(e)
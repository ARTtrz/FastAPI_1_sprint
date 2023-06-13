from typing import Any

from pydantic import BaseSettings
from pymongo import MongoClient


class Config(BaseSettings):
    CORS_ORIGINS: list[str] = ["*"]
    CORS_HEADERS: list[str] = ["*"]
    CORS_METHODS: list[str] = ["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"]

    MONGOHOST: str = "localhost"
    MONGOPORT: str = "27017"
    MONGOUSER: str = "root"
    MONGOPASSWORD: str = "password"
    MONGODATABASE: str = "fastapi"


# environmental variables
env = Config()

# FastAPI configurations
fastapi_config: dict[str, Any] = {
    "title": "Nfactorial",
}

# MongoDB connection
client = MongoClient(
    # f"mongodb://{env.MONGOUSER}:{env.MONGOPASSWORD}@{env.MONGOHOST}:{env.MONGOPORT}/"
    f"mongodb+srv://artemkim2006:Artyom_2006@cluster0.rescgtm.mongodb.net/?retryWrites=true&w=majority"
)

# MongoDB database
database = client[env.MONGODATABASE]

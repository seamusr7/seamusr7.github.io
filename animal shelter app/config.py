from dotenv import load_dotenv
import os

# Load environment variables from .env file if present
load_dotenv()

class Config:
    MONGO_URI = os.getenv("MONGO_URI")
    DATABASE_NAME = os.getenv("DATABASE_NAME")
    ANIMALS_COLLECTION = os.getenv("ANIMALS_COLLECTION")
    USERS_COLLECTION = os.getenv("USERS_COLLECTION")

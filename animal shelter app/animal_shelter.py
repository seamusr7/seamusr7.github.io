from pymongo import MongoClient
from config import Config

class AnimalShelter:
    def __init__(self):
        # MongoDB Atlas connection using environment variables from Config
        self.client = MongoClient(Config.MONGO_URI)
        self.database = self.client[Config.DATABASE_NAME]
        self.collection = self.database[Config.ANIMALS_COLLECTION]
        self.users = self.database[Config.USERS_COLLECTION]  # Collection for users

    def create(self, data):
        if data is not None:
            result = self.collection.insert_one(data)
            return result.inserted_id is not None
        else:
            raise Exception("Nothing to save because data parameter is empty")

    def read(self, query):
        data = self.collection.find(query)
        return list(data)

    def update(self, query, update_data):
        result = self.collection.update_many(query, {'$set': update_data})
        return result.modified_count

    def delete(self, query):
        result = self.collection.delete_many(query)
        return result.deleted_count

    # User management methods
    def register_user(self, username, password):
        if username and password:
            user = {"username": username, "password": password}
            result = self.users.insert_one(user)
            return result.inserted_id is not None
        else:
            raise Exception("Username or password is empty")

    def login_user(self, username, password):
        user = self.users.find_one({"username": username, "password": password})
        return user is not None

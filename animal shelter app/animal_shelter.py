from pymongo import MongoClient
from config import Config


class AnimalShelter:
    def __init__(self):
        """
        Initializes the AnimalShelter instance.
        Connects to the MongoDB Atlas using credentials from the Config class.
        Sets up the database and collection references.
        """
        self.client = MongoClient(Config.MONGO_URI)
        self.database = self.client[Config.DATABASE_NAME]
        self.collection = self.database[Config.ANIMALS_COLLECTION]
        self.users = self.database[Config.USERS_COLLECTION]  # Collection for users

    def create(self, data):
        """
        Creates a new document in the animals collection.

        :param data: A dictionary representing the animal data to be inserted.
        :return: Boolean indicating whether the insert was successful.
        :raises Exception: If the data parameter is empty.
        """
        if data is not None:
            result = self.collection.insert_one(data)
            return result.inserted_id is not None
        else:
            raise Exception("Nothing to save because data parameter is empty")

    def read(self, query):
        """
        Reads documents from the animals collection based on the query.

        :param query: A dictionary representing the MongoDB query.
        :return: A list of documents matching the query.
        """
        data = self.collection.find(query)
        return list(data)

    def update(self, query, update_data):
        """
        Updates documents in the animals collection based on the query.

        :param query: A dictionary representing the MongoDB query.
        :param update_data: A dictionary with the fields to be updated.
        :return: The number of documents that were modified.
        """
        result = self.collection.update_many(query, {'$set': update_data})
        return result.modified_count

    def delete(self, query):
        """
        Deletes documents from the animals collection based on the query.

        :param query: A dictionary representing the MongoDB query.
        :return: The number of documents that were deleted.
        """
        result = self.collection.delete_many(query)
        return result.deleted_count

    def register_user(self, username, password):
        """
        Registers a new user in the users collection.

        :param username: The username of the new user.
        :param password: The password of the new user.
        :return: Boolean indicating whether the insert was successful.
        :raises Exception: If the username or password is empty.
        """
        if username and password:
            user = {"username": username, "password": password}
            result = self.users.insert_one(user)
            return result.inserted_id is not None
        else:
            raise Exception("Username or password is empty")

    def login_user(self, username, password):
        """
        Authenticates a user based on the provided credentials.

        :param username: The username of the user.
        :param password: The password of the user.
        :return: Boolean indicating whether the login was successful.
        """
        user = self.users.find_one({"username": username, "password": password})
        return user is not None

    def quick_sort(self, arr, key=lambda x: x):
        """
        Performs quick sort on the given array.

        :param arr: The list of items to be sorted.
        :param key: A function that serves as a key for the sort comparison (default is identity function).
        :return: A new list sorted based on the key function.
        """
        if len(arr) <= 1:
            return arr
        else:
            pivot = arr[len(arr) // 2]
            left = [x for x in arr if key(x) < key(pivot)]
            middle = [x for x in arr if key(x) == key(pivot)]
            right = [x for x in arr if key(x) > key(pivot)]
            return self.quick_sort(left, key) + middle + self.quick_sort(right, key)

    def merge_sort(self, array, key=lambda x: x):
        """
        Performs merge sort on the given array.

        :param array: The list of items to be sorted.
        :param key: A function that serves as a key for the sort comparison (default is identity function).
        :return: A new list sorted based on the key function.
        """
        if len(array) <= 1:
            return array
        mid = len(array) // 2
        left_half = self.merge_sort(array[:mid], key)
        right_half = self.merge_sort(array[mid:], key)
        return self._merge(left_half, right_half, key)

    def _merge(self, left, right, key):
        """
        Merges two sorted lists into one sorted list.

        :param left: The left half of the list.
        :param right: The right half of the list.
        :param key: A function that serves as a key for the sort comparison.
        :return: A merged and sorted list based on the key function.
        """
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if key(left[i]) <= key(right[j]):
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

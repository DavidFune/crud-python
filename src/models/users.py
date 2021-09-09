from pymongo import MongoClient

client = MongoClient("0.0.0.0", 27020)

db = client.db_crud_python
users = db.Users


def get_users() -> list:
    list_users = list(users.find())
    return list_users

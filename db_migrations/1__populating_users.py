from pymongo import MongoClient


client = MongoClient("0.0.0.0", 27020)

db = client.db_crud_python

db.Users.insert_many([
    {"name": "test-1", "email": "test-1@smart.com",
        "password": "E150A1EC81E8E93E1EAE2C3A77E66EC6DBD6A3B460F89C1D08AECF422EE401A0"},
    {"name": "test-2", "email": "test-2@smart.com",
        "password": "E150A1EC81E8E93E1EAE2C3A77E66EC6DBD6A3B460F89C1D08AECF422EE401A0"},
    {"name": "test-3", "email": "test-3@smart.com",
        "password": "E150A1EC81E8E93E1EAE2C3A77E66EC6DBD6A3B460F89C1D08AECF422EE401A0"},
    {"name": "test-4", "email": "test-4@smart.com",
        "password": "E150A1EC81E8E93E1EAE2C3A77E66EC6DBD6A3B460F89C1D08AECF422EE401A0"}
])

from pymongo import MongoClient
client = MongoClient('localhost', 27017)

db = client.eve
entries = db.entries
users = db.users
#insertion données
import requests
from pymongo import MongoClient

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)
data = response.json()

client = MongoClient('mongodb://localhost:27017/')

db = client.userName

collection = db.users

result = collection.insert_many(data)

print("IDs insères :", result.inserted_ids)

client.close()
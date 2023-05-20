import requests

from pymongo import MongoClient

user_ids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

base_url = "https://jsonplaceholder.typicode.com/posts/"

client = MongoClient('mongodb://localhost:27017/')

db = client.userName

collection = db.postId

for user_id in user_ids:

    url = base_url + str(user_id)
    
    response = requests.get(url)
    
    if response.status_code == 200:

        user_data = response.json()
        
        result = collection.insert_one(user_data)
        print("ID inséré :", result.inserted_id)
    else:
        print(f"Erreur de requête pour l'ID {user_id} :", response.status_code)

client.close()

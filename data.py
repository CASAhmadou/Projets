from flask import Flask, jsonify
from pymongo import MongoClient
from bson.json_util import dumps

app = Flask(__name__)

client = MongoClient('mongodb://localhost:27017/')
db = client['userName']
collection = db['users']

@app.route('/users', methods=['GET'])
def get_users():
    users = list(collection.find())
    return dumps(users)

if __name__ == '__main__':
    app.run(debug=True)
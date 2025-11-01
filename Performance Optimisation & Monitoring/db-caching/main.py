from fastapi import FastAPI
from pydantic import BaseModel
import redis
import sqlite3
import json
import hashlib

app = FastAPI()

redis_client = redis.Redis(host='localhost', port=6379, db=0)

# Database connection
def get_db_connection():
    conn = sqlite3.connect('example.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL
        )
    ''')
    cursor.execute("INSERT INTO items (name, age) VALUES ('Alice', 30), ('Bob', 25), ('Charlie', 35)")
    cursor.execute("INSERT INTO items (name, age) VALUES ('Vijay', 35), ('Babu', 45), ('Chaitanya', 55)")
    conn.commit()
    conn.close()
init_db()

class UserQuery(BaseModel):
    user_id: int


def generate_cache_key(query: UserQuery) -> str:
    data_string = json.dumps(query.dict(), sort_keys=True)
    return hashlib.md5(data_string.encode('utf-8')).hexdigest()

@app.post('/get-user')
def get_user(query: UserQuery):
    cache_key = generate_cache_key(query)
    cached_result = redis_client.get(cache_key)

    if cached_result:
        print("Cache hit. Returning cached result.")
        return json.loads(cached_result)

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM items WHERE id = ?", (query.user_id,))
    user = cursor.fetchone()
    conn.close()

    if user:
        result = {"id": user["id"], "name": user["name"], "age": user["age"]}
        redis_client.set(cache_key, json.dumps(result))
        return result

    return {"error": "User not found"}, 404

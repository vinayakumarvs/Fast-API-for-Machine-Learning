import redis
import hashlib
import json
import httpx
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

redis_client = redis.Redis(host='localhost', port=6379, db=0)

class PostRequest(BaseModel):
    post_id : int

def make_cache_key(post_id: int) -> str:
    key_string = json.dumps({"post_id": post_id}, sort_keys=True)
    return hashlib.md5(key_string.encode('utf-8')).hexdigest()

@app.post('/get-post')
async def get_post(data: PostRequest):
    cache_key = make_cache_key(data.post_id)

    cached_data = redis_client.get(cache_key)
    if cached_data:
        print('Served from Redis cache!')
        return json.loads(cached_data)
    
    print('Calling external API...')
    async with httpx.AsyncClient() as client:
        response = await client.get(f"https://jsonplaceholder.typicode.com/posts/{data.post_id}")
        if response.status_code != 200:
            return {'error': 'Post not found!'}
        
    post_data = response.json()
    redis_client.setex(cache_key, 600, json.dumps(post_data))
    print('Fetched and stored in Cache!')
    return post_data
import redis

r = redis.Redis(host='localhost', port=6379, db=0)

try:
    r.ping()
    print("Connected to Redis successfully!")
except redis.ConnectionError:
    print("Failed to connect to Redis.")

# Example operation: Set and get a value
r.set('framework', 'FastAPI')
value = r.get('framework')
print(f"Value from Redis: {value.decode('utf-8')}")
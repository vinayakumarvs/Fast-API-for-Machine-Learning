import time
from fastapi import FastAPI



app = FastAPI()

def computation(n: int) -> int:
    total = 0
    for i in range(n):
        total += i ** 2
        time.sleep(1)  # Simulate a time-consuming task
    return total

@profile
def process_data(n: int) -> int:
    return computation(n)

@app.get("/profiling")
def profiling_endpoint(n: int = 5) -> dict:
    result = process_data(n)
    return {"result": result}
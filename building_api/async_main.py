from fastapi import FastAPI
from async_demo import run_task
import asyncio
app = FastAPI()

@app.get("/wait")
async def wait():
    await run_task("Main", 4)
    return {"message": "Waited for 4 seconds"}
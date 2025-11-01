import time
import logging
from fastapi import FastAPI, Request

app = FastAPI()
logging.basicConfig(level=logging.INFO, 
                    format='[%(asctime)s - %(levelname)s] (lineno: %(lineno)d) - %(levelname)s - %(message)s', 
                    datefmt='%Y-%m-%d %H:%M:%S')

logger = logging.getLogger('profiler')

app = FastAPI()

@app.middleware("http")
async def ad_timing_middleware(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    logger.info(f"Request: {request.method} {request.url} completed in {process_time:.4f} seconds")
    return response

@app.get("/")
def home():
    return {"message": "Welcome to the Time Profiling Demo!"}

@app.get('/slow')
async def slow_endpoint():
    time.sleep(2)
    return {"message": "This is a slow endpoint!"}

@app.get('/fast')
async def fast_endpoint():
    return {"message": "This is a fast endpoint!"}
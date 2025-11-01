import os
import time
import cProfile
import datetime
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

PROFILES_DIR = 'profiles'
os.makedirs(PROFILES_DIR, exist_ok=True)

app = FastAPI()

@app.middleware("http")
async def create_profile(request: Request, call_next):
    profile = cProfile.Profile()
    profile.enable()
    
    response = await call_next(request)
    
    profile.disable()
    
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    profile_filename = os.path.join(PROFILES_DIR, f"profile_{timestamp}.prof")
    profile.dump_stats(profile_filename)
    print(f"Profile saved to {profile_filename}")
    
    return response

@app.get("/")
def home():
    return JSONResponse(content={"message": "Welcome to the FastAPI profiling demo!"})

@app.get("/compute")
async def compute():
    # Simulate a CPU-bound task
    total = 0
    for i in range(1, 1000000):
        total += i ** 0.5
    return JSONResponse(content={"result": total})
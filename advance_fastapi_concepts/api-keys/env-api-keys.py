from fastapi import FastAPI, Depends, HTTPException, Header
from pydantic_settings import BaseSettings


app = FastAPI()

class Settings(BaseSettings):
    API_KEY: str
    class Config:
        env_file = ".env"

settings = Settings()

def get_api_key(
    api_key: str = Header(..., description="API Key for authentication")
):
    if api_key == settings.API_KEY:
        return api_key
    else:
        raise HTTPException(status_code=403, detail="Forbidden")
    
@app.get("/get-data")
def get_data(api_key: str = Depends(get_api_key)):
    return {"message": "This is protected data"}



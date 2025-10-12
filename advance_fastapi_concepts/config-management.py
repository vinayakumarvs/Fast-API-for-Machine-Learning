from fastapi import FastAPI, Depends

app = FastAPI()

class Settings:
    def __init__(self):
        self.api_key = "your_api_key"
        self.debug = True

def get_settings():
    return Settings()

@app.get("/config")
async def get_config(settings: Settings = Depends(get_settings)):
    return {"api_key": settings.api_key, "debug": settings.debug}
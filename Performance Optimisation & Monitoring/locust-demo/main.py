from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class InputData(BaseModel):
    feature1: float
    feature2: float

@app.get("/")
def home():
    return {"message": "Welcome to the FastAPI application Locust Demo!"}

@app.post("/predict")
def predict(data: InputData):
    # Dummy prediction logic
    prediction = data.feature1 + data.feature2
    return {"prediction": prediction}
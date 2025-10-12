from fastapi import FastAPI
from pydantic import BaseModel
from model import model
import numpy as np


app = FastAPI()

class IrisFeatures(BaseModel):
    SepalLengthCm: float
    SepalWidthCm: float
    PetalLengthCm: float
    PetalWidthCm: float

@app.post("/predict")
def predict(features: IrisFeatures):
    features = np.array([[features.SepalLengthCm, features.SepalWidthCm, features.PetalLengthCm, features.PetalWidthCm]])
    prediction = model.predict(features)
    return {"prediction": int(prediction[0])}
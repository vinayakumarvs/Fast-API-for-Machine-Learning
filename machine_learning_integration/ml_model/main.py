from fastapi import FastAPI
from schemas import InputSchema, OutputSchema
from predict import make_prediction, make_batch_predictions
from typing import List

app = FastAPI()

@app.get("/")
def index():
    return {"message": "Welcome to the House Price Prediction API"}

@app.post("/predict", response_model=OutputSchema)
def predict(input_data: InputSchema):
    predicted_price = make_prediction(input_data.model_dump())
    return OutputSchema(predicted_price=round(predicted_price, 2))

@app.post("/predict/batch", response_model=List[OutputSchema])
def batch_predict(input_data: List[InputSchema]):
    predictions = make_batch_predictions([data.model_dump() for data in input_data])
    return [OutputSchema(predicted_price=round(price, 2)) for price in predictions]
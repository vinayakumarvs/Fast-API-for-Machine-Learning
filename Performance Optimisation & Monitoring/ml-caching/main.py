from fastapi import FastAPI
from pydantic import BaseModel
import redis
import json
import hashlib
import joblib

app = FastAPI()

redis_client = redis.Redis(host='localhost', port=6379, db=0)

model = joblib.load('model.joblib')

class PredictionRequest(BaseModel):
    longitude: float
    latitude: float
    housing_median_age: float
    total_rooms: float
    total_bedrooms: float
    population: float
    households: float
    median_income: float
    
    def to_list(self):
        return [
            self.longitude,
            self.latitude,
            self.housing_median_age,
            self.total_rooms,
            self.total_bedrooms,
            self.population,
            self.households,
            self.median_income,
        ]
    
    

def generate_cache_key(data: PredictionRequest) -> str:
    data_string = json.dumps(data.dict(), sort_keys=True)
    return hashlib.md5(data_string.encode('utf-8')).hexdigest()

@app.post("/predict")
async def predict(request: PredictionRequest):
    cache_key = generate_cache_key(request)
    
    cached_result = redis_client.get(cache_key)
    if cached_result:
        print("Cache hit. Returning cached result.")
        return {"Predicted House Price": json.loads(cached_result)}
    
    input_data = [request.to_list()]
    prediction = model.predict(input_data).tolist()
    
    redis_client.set(cache_key, json.dumps(prediction))
    
    return {"Predicted House Price": prediction}
import joblib
import numpy as np
from typing import List

saved_model = joblib.load('linear_regression_model.joblib')
print('Loaded the model from the joblib file')

def make_prediction(input_data: dict) -> float:
    features = np.array([[
        input_data['longitude'],
        input_data['latitude'],
        input_data['housing_median_age'],
        input_data['total_rooms'],
        input_data['total_bedrooms'],
        input_data['population'],
        input_data['households'],
        input_data['median_income']]
    ])
    return saved_model.predict(features)[0]

# Define Batch Prediction Function
def make_batch_predictions(input_data: List[dict]) -> np.array:
    features = np.array([[
        data['longitude'],
        data['latitude'],
        data['housing_median_age'],
        data['total_rooms'],
        data['total_bedrooms'],
        data['population'],
        data['households'],
        data['median_income']]
    for data in input_data])
    return saved_model.predict(features).tolist()
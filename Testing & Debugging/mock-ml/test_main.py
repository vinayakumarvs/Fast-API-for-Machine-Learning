from fastapi.testclient import TestClient
from unittest.mock import patch
from main import app
import numpy as np

client = TestClient(app)

def test_predict_with_mock_data():
    with patch('model.model.predict') as mock_predict:
        mock_predict.return_value = [1]  # Mocking the prediction to always return class '1'
        
        response = client.post(
            "/predict",
            json={
                "SepalLengthCm": 5.1,
                "SepalWidthCm": 3.5,
                "PetalLengthCm": 1.4,
                "PetalWidthCm": 0.2
            }
        )
        
        assert response.status_code == 200
        assert response.json() == {"prediction": 1}
        # mock_predict.assert_called_once_with(np.array([[5.1, 3.5, 1.4, 0.2]]))


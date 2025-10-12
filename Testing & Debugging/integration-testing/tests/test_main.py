from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_loan_eligibility_eligible():
    response = client.post("/loan_eligibility", json={
        "income": 50000,
        "age": 30,
        "employment_status": "employed"
    })
    assert response.status_code == 200
    assert response.json() == {"eligible": True}

def test_loan_eligibility_ineligible_due_to_age():
    response = client.post("/loan_eligibility", json={
        "income": 50000,
        "age": 17,
        "employment_status": "employed"
    })
    assert response.status_code == 200
    assert response.json() == {"eligible": False}

    response = client.post("/loan_eligibility", json={
        "income": 50000,
        "age": 66,
        "employment_status": "employed"
    })
    assert response.status_code == 200
    assert response.json() == {"eligible": False}
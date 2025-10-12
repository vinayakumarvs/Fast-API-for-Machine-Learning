from fastapi import FastAPI
from pydantic import BaseModel
from app.logic import is_eligible_for_loan

app = FastAPI()

class LoanApplication(BaseModel):
    income: float
    age: int
    employment_status: str

@app.post("/loan_eligibility")
def check_loan_eligibility(application: LoanApplication):
    eligibility = is_eligible_for_loan(
        application.income, application.age, application.employment_status
    )
    return {"eligible": eligibility}


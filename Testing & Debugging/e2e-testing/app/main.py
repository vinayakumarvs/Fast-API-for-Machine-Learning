from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class LoanApplication(BaseModel):
    age: int
    income: float
    employment_status: str

@app.post("/loan_eligibility")
def check_loan_eligibility(application: LoanApplication):
    if (application.income >= 30000 and 
        application.age >= 21 and 
        application.employment_status in ["employed", "self-employed"]):
        return {"eligible": True}
    else:
        return {"eligible": False}
    

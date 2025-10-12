from fastapi import FastAPI, HTTPException, Depends
from models import Employee
from schemas import EmployeeCreate, EmployeeUpdate, EmployeeOut
from database import SessionLocal, engine, Base
from crud import get_employees, get_employee, create_employee, update_employee, delete_employee
from sqlalchemy.orm import Session
from typing import List

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoints
# Create Employee
@app.post("/employees/", response_model=EmployeeOut)
def create_employee_endpoint(employee: EmployeeCreate, db: Session = Depends(get_db)):
    return create_employee(db=db, employee=employee)

# Read All Employees
@app.get("/employees/", response_model=List[EmployeeOut])
def read_employees(db: Session = Depends(get_db)):
    return get_employees(db=db)

# Read Single Employee
@app.get("/employees/{employee_id}", response_model=EmployeeOut)
def read_employee(employee_id: int, db: Session = Depends(get_db)):
    db_employee = get_employee(db=db, employee_id=employee_id)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return db_employee

# Update Employee
@app.put("/employees/{employee_id}", response_model=EmployeeOut)
def update_employee_endpoint(employee_id: int, employee: EmployeeUpdate, db: Session = Depends(get_db)):
    db_employee = update_employee(db=db, employee_id=employee_id, employee=employee)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return db_employee

# Delete Employee
@app.delete("/employees/{employee_id}", response_model=EmployeeOut)
def delete_employee_endpoint(employee_id: int, db: Session = Depends(get_db)):
    db_employee = delete_employee(db=db, employee_id=employee_id)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return db_employee
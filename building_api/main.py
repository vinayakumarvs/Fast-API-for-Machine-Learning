from fastapi import FastAPI, HTTPException
from models import Employee
from typing import List


employee_db: List[Employee] = []

app = FastAPI()

# 1. Read all employees
@app.get("/employees", response_model=List[Employee])
async def get_employees():
    return employee_db

# 2. Read an employee by ID
@app.get("/employees/{employee_id}", response_model=Employee)
async def get_employee(employee_id: int):
    for index, emp in enumerate(employee_db):
        if emp.id == employee_id:
            return emp
    raise HTTPException(status_code=404, detail="Employee not found")

# 3. Create a new employee
@app.post("/employees", response_model=Employee)
async def create_employee(new_employee: Employee):
    for emp in employee_db:
        if emp.id == new_employee.id:
            raise HTTPException(status_code=400, detail="Employee with this ID already exists")
    employee_db.append(new_employee)
    return new_employee

# 4. Update an existing employee
@app.put("/employees/{employee_id}", response_model=Employee)
async def update_employee(employee_id: int, updated_employee: Employee):
    for index, emp in enumerate(employee_db):
        if emp.id == employee_id:
            employee_db[index] = updated_employee
            return updated_employee
    raise HTTPException(status_code=404, detail="Employee not found")

# 5. Delete an employee
@app.delete("/employees/{employee_id}")
async def delete_employee(employee_id: int):
    for index, emp in enumerate(employee_db):
        if emp.id == employee_id:
            del employee_db[index]
            return {"detail": "Employee deleted"}
    raise HTTPException(status_code=404, detail="Employee not found")
    
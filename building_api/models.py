from pydantic import BaseModel, Field
from typing import Optional

class Employee(BaseModel):
    id: int = Field(..., gt=0, title="Employee ID", description="The unique identifier for the employee, must be greater than 0")
    name: str = Field(..., min_length=3, title="Employee Name", description="The name of the employee")
    department: str = Field(..., min_length=2, title="Department", description="The department where the employee works")
    age: int = Field(..., gt=18, title="Age", description="The age of the employee, must be greater than 18")
    salary: Optional[float] = Field(None, gt=10, title="Salary", description="The salary of the employee, must be greater than 10 if provided")
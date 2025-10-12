def is_eligible_for_loan(income: float, age: int, employment_status: str) -> bool:
    return income >= 30000 and 18 <= age <= 65 and employment_status == 'employed'


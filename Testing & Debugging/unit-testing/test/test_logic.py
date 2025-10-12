import pytest
from app.logic import is_eligible_for_loan

def test_eligible_user():
    assert is_eligible_for_loan(50000, 30, 'employed') == True

def test_ineligible_user_due_to_age():
    assert is_eligible_for_loan(50000, 17, 'employed') == False
    assert is_eligible_for_loan(50000, 66, 'employed') == False

def test_ineligible_user_due_to_income():
    assert is_eligible_for_loan(25000, 30, 'employed') == False

def test_ineligible_user_due_to_employment_status():
    assert is_eligible_for_loan(50000, 30, 'unemployed') == False

def test_edge_case_age():
    assert is_eligible_for_loan(50000, 18, 'employed') == True
    assert is_eligible_for_loan(50000, 65, 'employed') == True
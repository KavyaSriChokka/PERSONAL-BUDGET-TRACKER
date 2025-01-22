import pytest
from project import calculate_total_expenses, calculate_remaining_budget

def test_calculate_total_expenses():
    expenses = [100.0, 50.5, 25.75]
    assert calculate_total_expenses(expenses) == 176.25

def test_calculate_remaining_budget():
    budget = 500.0
    total_expenses = 300.0
    assert calculate_remaining_budget(budget, total_expenses) == 200.0

def test_calculate_remaining_budget_no_expenses():
    budget = 300.0
    total_expenses = 0.0
    assert calculate_remaining_budget(budget, total_expenses) == 300.0
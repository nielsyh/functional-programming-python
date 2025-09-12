# total_salary_calculator.py

# Import the 'reduce' function from the functools module for aggregation.
from functools import reduce
from typing import List, Dict, Any, Callable

# --- Data ---
# A list of dictionaries, where each dictionary represents an employee.
Employee = Dict[str, Any]
employees: List[Employee] = [
    {'name': 'Alice', 'role': 'Junior Developer', 'years_at_company': 2, 'salary': 50000},
    {'name': 'Bob', 'role': 'Senior Developer', 'years_at_company': 7, 'salary': 90000},
    {'name': 'Charlie', 'role': 'Manager', 'years_at_company': 10, 'salary': 120000},
    {'name': 'David', 'role': 'Senior Developer', 'years_at_company': 4, 'salary': 85000},
    {'name': 'Eve', 'role': 'Senior Developer', 'years_at_company': 6, 'salary': 95000},
    {'name': 'Frank', 'role': 'Junior Developer', 'years_at_company': 1, 'salary': 48000},
    {'name': 'Grace', 'role': 'Senior Developer', 'years_at_company': 9, 'salary': 105000},
]

# --- Solution ---
# Step 1: Filter the list of employees.
# We use a lambda function to define our filtering criteria. It checks if
# the employee's role is 'Senior Developer' AND their years at the company
# are greater than 5.
# The `filter()` function returns a `filter` object (an iterator), not a list.
eligible_employees_filter = filter(
    lambda emp: emp['role'] == 'Senior Developer' and emp['years_at_company'] > 5,
    employees
)
# Hint: At this point, `eligible_employees_filter` contains Bob, Eve, and Grace.

# Step 2: Map the filtered list to their salaries.
# We use a lambda function to extract the 'salary' from each employee dictionary.
# The `map()` function returns a `map` object (an iterator), not a list.
salaries_map = map(
    lambda emp: emp['salary'],
    eligible_employees_filter
)
# Hint: `salaries_map` now yields 90000, 95000, and 105000.

# Step 3: Reduce the salaries to a single total.
# We use a lambda function to cumulatively sum the elements.
# The `reduce()` function applies the function to the first two items, then applies
# it to the result and the next item, and so on, until a single value is returned.
total_salary = reduce(
    lambda x, y: x + y,
    salaries_map
)

# --- Test ---
# The expected total salary is 90000 + 95000 + 105000 = 290000.
expected_total = 290000
assert total_salary == expected_total

print(f"Calculated Total Salary: {total_salary}")
print(f"Expected Total Salary:   {expected_total}")
print("\nSuccess! The solution is correct.")
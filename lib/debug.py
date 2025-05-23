#!/usr/bin/env python3

from __init__ import CONN, CURSOR
from department import Department
from employee import Employee
import ipdb

def reset_database():
    # Drop tables if they exist
    Employee.drop_table()
    Department.drop_table()
    
    # Create new tables
    Department.create_table()
    Employee.create_table()

    # Create seed departments
    payroll = Department.create("Payroll", "Building A, 5th Floor")
    human_resources = Department.create(
        "Human Resources", "Building C, East Wing")
    
    # Create seed employees
    employees = [
        ("Amir", "Accountant", payroll.id),
        ("Bola", "Manager", payroll.id),
        ("Charlie", "Manager", human_resources.id),
        ("Dani", "Benefits Coordinator", human_resources.id),
        ("Hao", "New Hires Coordinator", human_resources.id)
    ]
    
    for name, job_title, dept_id in employees:
        Employee.create(name, job_title, dept_id)

    print("Database reset complete!")
    print(f"Created {len(Department.get_all())} departments")
    print(f"Created {len(Employee.get_all())} employees")

if __name__ == '__main__':
    reset_database()
    ipdb.set_trace()
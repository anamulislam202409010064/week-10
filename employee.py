# employee.py
# Collect employee information


def get_employee():
    print("===== EMPLOYEE INFORMATION =====")

    employee_name = input("Employee Name: ")
    employee_id = input("Employee ID: ")

    basic_salary = float(input("Basic Salary (RM): "))
    allowance = float(input("Allowance (RM): "))
    years_worked = int(input("Years Worked: "))
    overtime_hours = float(input("Overtime Hours: "))

    return (
        employee_name,
        employee_id,
        basic_salary,
        allowance,
        years_worked,
        overtime_hours
    )
# main.py
# Main program

from employee import get_employee
from salary import calculate_net_salary
from report import print_report


def main():
    employee = get_employee()

    name = employee[0]
    employee_id = employee[1]
    basic_salary = employee[2]
    allowance = employee[3]
    years_worked = employee[4]
    overtime_hours = employee[5]

    salary_details = calculate_net_salary(
        basic_salary,
        allowance,
        overtime_hours,
        years_worked
    )

    print_report(
        name,
        employee_id,
        salary_details
    )


main()
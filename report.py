# report.py
# Create a function to print report


def print_report(name, employee_id, salary_details):
    print("\n========== SALARY REPORT ==========")

    print("Employee Name :", name)
    print("Employee ID   :", employee_id)

    print("-----------------------------------")

    print(
        "Basic Salary  : RM",
        format(salary_details["basic_salary"], ".2f")
    )

    print(
        "Allowance     : RM",
        format(salary_details["allowance"], ".2f")
    )

    print(
        "Overtime Pay  : RM",
        format(salary_details["overtime_pay"], ".2f")
    )

    print(
        "Reward        : RM",
        format(salary_details["reward"], ".2f")
    )

    print(
        "Gross Salary  : RM",
        format(salary_details["gross_salary"], ".2f")
    )

    print(
        "EPF (11%)     : RM",
        format(salary_details["epf"], ".2f")
    )

    print(
        "SOCSO (0.5%)  : RM",
        format(salary_details["socso"], ".2f")
    )

    print("-----------------------------------")

    print(
        "Net Salary    : RM",
        format(salary_details["net_salary"], ".2f")
    )

    print("===================================")
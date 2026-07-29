# salary.py
# Create functions to calculate salary

EPF_RATE = 0.11
SOCSO_RATE = 0.005
OVERTIME_RATE = 25.00
LOYALTY_REWARD = 100.00


def calculate_epf(gross_salary):
    return gross_salary * EPF_RATE


def calculate_socso(gross_salary):
    return gross_salary * SOCSO_RATE


def calculate_overtime(overtime_hours):
    return overtime_hours * OVERTIME_RATE


def calculate_reward(years_worked):
    if years_worked > 3:
        return LOYALTY_REWARD
    else:
        return 0.00


def calculate_net_salary(
    basic_salary,
    allowance,
    overtime_hours,
    years_worked
):
    overtime_pay = calculate_overtime(overtime_hours)
    reward = calculate_reward(years_worked)

    gross_salary = (
        basic_salary
        + allowance
        + overtime_pay
        + reward
    )

    epf = calculate_epf(gross_salary)
    socso = calculate_socso(gross_salary)

    net_salary = gross_salary - epf - socso

    return {
        "basic_salary": basic_salary,
        "allowance": allowance,
        "overtime_pay": overtime_pay,
        "reward": reward,
        "gross_salary": gross_salary,
        "epf": epf,
        "socso": socso,
        "net_salary": net_salary
    }
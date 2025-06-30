# Shamir Bhandari
# 6/28/2025
# P3H2
# Worker pay calculator

employee_name = input("Enter employee's name:")
hours_worked = float(input("Enter number of hours worked:"))
pay_rate = float(input("Enter employee's pay rate:"))

if hours_worked > 40:
    overtime_hours = hours_worked - 40
    regular_hours = 40
else:
    overtime_hours = 0
    regular_hours = hours_worked

regular_pay = regular_hours * pay_rate
overtime_pay = overtime_hours * (1.5 * pay_rate)
gross_pay = regular_pay + overtime_pay

print("------------------------------------------")
print(f"Employee Name:         {employee_name}")

print(f"Hours Worked:          {hours_worked}")
print(f"Pay Rate:              ${pay_rate:.2f}")
print(f"Overtime Hours:        {overtime_hours}")
print(f"Overtime Pay:          ${overtime_pay:.2f}")
print(f"Regular Pay:           ${regular_pay:.2f}")
print(f"Gross Pay:             ${gross_pay:.2f}")

print("------------------------------------------")






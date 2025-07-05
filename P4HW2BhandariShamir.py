# Shamir Bhandari
# 7/5/2025
# P4H2
# Worker pay calculator remastered with loop

#Initialize accumulators:
#       total_overtime = 0
#       total_regular = 0
#       total_gross   = 0
#       employee_count = 0
#
# 2. Start  loop:
#    WHILE employee_name is not "done":
#       a. Ask for employee's name.
#          - If name is "done", exit loop.
#       b. Prompt for hours_worked and pay_rate.
#
#       c. IF hours_worked > 40:
#             overtime_hours = hours_worked - 40
#             regular_hours = 40
#          ELSE:
#             overtime_hours = 0
#             regular_hours = hours_worked
#
#       d. Calculate:
#             regular_pay = regular_hours * pay_rate
#             overtime_pay = overtime_hours * 1.5 * pay_rate
#             gross_pay = regular_pay + overtime_pay
#
#       e. Add values to totals:
#             total_overtime += overtime_pay
#             total_regular += regular_pay
#             total_gross   += gross_pay
#             employee_count += 1
#
#       f. Display:
#             Employee name
#             Table-style output with hours worked, pay rate,
#             overtime hours/pay, regular pay, and gross pay
#
# 3. After loop ends, display final payroll summary:
#       - Total employees entered
#       - Total overtime pay
#       - Total regular pay
#       - Total gross pay
# -----------------------------------------------------------



total_overtime = 0.0
total_regular = 0.0
total_gross = 0.0
employee_count = 0
 
# loop
while True:
    employee_name = input("Enter employee's name (or 'done' to finish): ")
    if employee_name == "done":
        break

    hours_worked = float(input("Enter number of hours worked: "))
    pay_rate = float(input("Enter employee's pay rate: "))

    # Calculate hours
    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        regular_hours = 40
    else:
        overtime_hours = 0
        regular_hours = hours_worked

    # Calculate pay
    regular_pay = regular_hours * pay_rate
    overtime_pay = overtime_hours * (1.5 * pay_rate)
    gross_pay = regular_pay + overtime_pay

    # Update totals
    total_overtime += overtime_pay
    total_regular += regular_pay
    total_gross += gross_pay
    employee_count += 1

    # Display formatted output for the employee
    print(f"\nEmployee name: {employee_name}\n")
    print(f"{'Hours Worked':<15}{'Pay Rate':<12}{'OverTime':<12}"
          f"{'OverTime Pay':<16}{'RegHour Pay':<15}{'Gross Pay':<12}")
    print("-" * 83)  
    print(f"{hours_worked:<15.1f}"
        f"{pay_rate:<12.2f}"
        f"{overtime_hours:<12.1f}"
        f"${overtime_pay:<15.2f}"
        f"${regular_pay:<14.2f}"
        f"${gross_pay:<.2f}\n")

# Final summary output
print("=========== PAYROLL SUMMARY ===============")
print(f"Total Employees Entered:     {employee_count}")
print(f"Total Overtime Pay:          ${total_overtime:.2f}")
print(f"Total Regular Pay:           ${total_regular:.2f}")
print(f"Total Gross Pay:             ${total_gross:.2f}")
print("========================================")

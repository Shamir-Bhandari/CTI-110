#Shamir Bhandari
#7-12-2025
#PLAB5
#Self Check out




import random

def disperse_change(change):
    if change == 0:
        print("No change")
        return


    cents = int(change * 100)

    dollars = cents // 100
    cents %= 100

    quarters = cents // 25
    cents %= 25

    dimes = cents // 10
    cents %= 10

    nickels = cents // 5
    cents %= 5

    pennies = cents

    if dollars == 1:
        print("1 dollar")
    elif dollars > 1:
        print(f"{dollars} dollars")

    if quarters == 1:
        print("1 quarter")
    elif quarters > 1:
        print(f"{quarters} quarters")

    if dimes == 1:
        print("1 dime")
    elif dimes > 1:
        print(f"{dimes} dimes")

    if nickels == 1:
        print("1 nickel")
    elif nickels > 1:
        print(f"{nickels} nickels")

    if pennies == 1:
        print("1 penny")
    elif pennies > 1:
        print(f"{pennies} pennies")

def main():
    total_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"You owe: ${total_owed:.2f}")

    money_given = float(input("How much cash will you put in the selfcheck out?: $"))

    if money_given < total_owed:
        print("Insufficient payment. Transaction cancelled.")
        return

    change = round(money_given - total_owed, 2)
    print(f"Change to be returned: ${change:.2f}")

    disperse_change(change)

main()

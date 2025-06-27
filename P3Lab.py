#Shamir Bhandari
#6-27-2025
#PLAB3
#Change money efficently into dollors, Dimes, Nickels, And pennies

money = float(input("Enter amount of money: "))

if money == 0:
    print("No change")

cents = int(money * 100)
 
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



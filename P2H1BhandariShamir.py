#Shamir Bhandari
#6/20/2025
#P2H1
#Make a Budget figurer Neater

print("This program calculates and displays travel expenses")
print()
budget= int(input("Enter Your Budget:"))
print()


destination = input("Enter your travel destination:")

print()
gas= int(input("How much do you think you will spend on gas?:"))
print()
living= int(input("Approximately, how much will you spend on accomondation/hotel?:"))
print()
food= int(input("Last, how much do you need for food?:"))
print()
cost= gas + living + food
print()
balance= budget- cost

budget= float(budget)
gas=float(gas)
living=float(living)
food=float(food)
cost=float(cost)
balance=float(balance)

print("------------------Travel Expenses-----------------")

print(f"{'Location:':<20}{destination:>12}")
print(f"{'Initial Budget:':<20}{f'${budget:,.2f}':>12}")
print(f"{'Fuel:':<20}{f'${gas:,.2f}':>12}")
print(f"{'Accommodation:':<20}{f'${living:,.2f}':>12}")
print(f"{'Food:':<20}{f'${food:,.2f}':>12}")

print("--------------------------------------------------")
print(f"{'Remaining Balance:':<20}{f'${balance:,.2f}':>12}")


         
      

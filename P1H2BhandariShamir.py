#Shamir Bhandari
#6/12/2025
#P1H2
#Make a Budget figurer.

print("This program calculates and displays travel expenses")

budget= int(input("Enter Your Budget:"))


destination = input("Enter your travel destination:")


gas= int(input("How much do you think you will spend on gas?:"))


living= int(input("Approximately, how much will you spend on accomondation/hotel?:"))


food= int(input("Last, how much do you need for food?:"))

cost= gas + living + food

balance= budget- cost


print("------------------Travel Expenses-----------------")

print("Location:", destination)
print("Initial Budget:", budget)


print("Fuel:", gas)
print("Accomodation:", living)
print("Food:", food)

print("Remaining Balance:", balance)




         

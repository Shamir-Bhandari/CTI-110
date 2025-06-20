#Shamir Bhandari
#6/20/2025
#P2LAB2
#Car MPG Calculator

car= {"Camero": 18.12, "Prius": 52.36, "Model S": 110, "Silverado":26}

keys= car.keys()
print(keys)
print()

car_choice= input("Enter a vehicle to see it's mpg:")
print()

mpg= car[car_choice]

print(f"The  {car_choice} gets {mpg} mpg")
print()

miles_drive= float(input(f"How many miles will you drive the {car_choice}?:"))
print()
gal_need= miles_drive/mpg

print(f"{gal_need:.2f} gallon(s) of gas are needed to drive the {car_choice} {miles_drive} miles.")

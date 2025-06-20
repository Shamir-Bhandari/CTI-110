#Shamir Bhandari
#6/20/2025
#P2H2
#Trying to Grade Homework Faster

Module1= float(input("Enter grade for module 1: "))
Module2= float(input("Enter grade for module 2: "))
Module3= float(input("Enter grade for module 3: "))             
Module4= float(input("Enter grade for module 4: "))                   
Module5= float(input("Enter grade for module 5: "))
Module6= float(input("Enter grade for module 6: "))

grade_list=[Module1, Module2, Module3, Module4, Module5, Module6]

print("--------------------Results---------------------------------")

smallest=min(grade_list)
biggest=max(grade_list)
together=sum(grade_list)
avg_grade=sum(grade_list)/len(grade_list)

print(f"Lowest grade: {smallest}")
print(f"Higest grade: {biggest}")
print(f"Sum of grades: {together}")
print(f"Average: {avg_grade:.2f}")

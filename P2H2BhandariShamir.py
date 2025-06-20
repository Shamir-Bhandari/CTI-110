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

# Pseudocode: Grade Summary Program

# 1. tell the user to enter grade for Module 1
# 2. go from input to float and put in Module1
# 3. REPEAT steps 1–2 for Modules 2 through 6

# 4. CREATE a list called grade_list containing all six module grades

# 5. FIND the minimum value in grade_list and put into variable 'smallest'
# 6. FIND the maximum value in grade_list and put into variable 'biggest'
# 7. CALCULATE the sum of all grades in grade_list and put in 'together'
# 8. CALCULATE the average by dividing 'together' by the number of grades
#    put into result in 'avg_grade'

# 9. DISPLAY a title for the results

# 10. DISPLAY the lowest grade with a label
# 11. DISPLAY the highest grade with a label
# 12. DISPLAY the sum of grades with a label
# 13. DISPLAY the average grade with a label (formatted to 2 decimal places)

# 14. DISPLAY a closing line or separator

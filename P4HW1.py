#Shamir Bhandari
#7/4/2025
#P4HW1
#Building a loop in homework grader

# ------------------------------------------------------------
# Pseudocode:
# 1. Ask the user how many scores they want to enter.
# 2. Create an empty list called 'scores' to store valid scores.
# 3. Use a for loop to repeat input for the number of scores.
#    a. Inside the loop, use a while loop to validate the input.
#    b. If score is invalid (<0 or >100), prompt again until valid.
#    c. Once valid, add it to the 'scores' list.
# 4. After all scores are collected:
#    a. Find and display the lowest score.
#    b. Remove that score and show the modified list.
#    c. Calculate the average of the remaining scores.
#    d. Assign a letter grade based on the average:
#       90+ = A, 80-89 = B, 70-79 = C, 60-69 = D, below 60 = F.
# 5. Display the lowest score, modified list, average, and letter grade.
# ------------------------------------------------------------


# Get number of scores 
num_scores = int(input("How many scores would you like to enter? "))
scores = []

# Collect valid scores
for i in range(num_scores):
    attempt = 1
    while True:
        if attempt == 1:
            prompt = f"Enter score #{i + 1}: "
        else:
            prompt = f"Enter score #{i + 1} again: "
        
        entered_score = float(input(prompt))
        
        if 0 <= entered_score <= 100:
            scores.append(entered_score)
            break
        
        else:
            print("INVALID score entered.")
            print("Please enter a number between 0 and 100.")
            attempt += 1

# scores
lowest = min(scores)
adjusted_scores = scores.copy()
adjusted_scores.remove(lowest)
average = sum(adjusted_scores) / len(adjusted_scores)

# letter grade
if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"
    
# results
print("\n------------ Results ------------")
print(f"{'Lowest score:':20} {lowest:.2f}")
print(f"{'Modified scores:':20} {adjusted_scores}")
print(f"{'Scores average:':20} {average:.2f}")
print(f"{'Letter grade:':20} {grade}")
print("---------------------------------")

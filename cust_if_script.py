# Prompt the user for a numeric score
score = float(input("Enter your score: "))

# Determine the letter grade based on the score
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

# Print the letter grade
print(f"Your score of {score} corresponds to a grade of {grade}")


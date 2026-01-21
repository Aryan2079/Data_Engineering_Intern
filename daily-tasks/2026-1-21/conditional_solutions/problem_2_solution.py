# Conditional Problem 2:
# Write a program that takes a student’s marks and prints whether they got “Distinction” (≥80), “Pass” (≥40), or “Fail” (<40).

user_input = input("Enter your marks: ")

try:
    marks = int(user_input)
except ValueError:
    print(f"Error: value is not a valid integer. Please try again.")

if marks <40:
    print("Fail")
elif marks >= 40 and marks<80:
    print("Pass")
elif marks >=80:
    print("Distinction")
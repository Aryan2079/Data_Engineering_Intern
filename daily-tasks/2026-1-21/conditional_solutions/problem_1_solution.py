# Conditional Problem 1:
# Write a program to check if a number is positive, negative, or zero.

user_input = int(input("please enter your number: "))

try:
    num = int(user_input)
except ValueError:
    print(f"Error: value is not a valid integer. Please try again.")


if(num>0):
    print('number is positive')
elif(num<0):
    print('number is negative')
else:
    print('number is zero')
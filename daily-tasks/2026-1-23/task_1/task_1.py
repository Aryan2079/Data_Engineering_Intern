# task 1: Write a recursive function to calculate the factorial of a number.

def factorial(num):
    if num < 0:
        raise ValueError("Please enter a positive number")
    if num == 0:
        return 0
    if num==1:
        return 1
    return num * factorial(num-1)

print(factorial(-1))
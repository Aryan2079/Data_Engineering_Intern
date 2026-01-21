# Function Problem 1:
# Write a function that takes two numbers and returns their greatest common divisor (GCD).

def gcd(a, b):
    while(a != b):
        if a > b:
            a = a - b
        elif b > a:
            b = b - a

    return a

print(gcd(24,18))
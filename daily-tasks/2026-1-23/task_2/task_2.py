# task 2:  Write a recursive function to find the nth Fibonacci number.

def fibo(n):
    if n==1:
        return 0
    if n==2:
        return 1
    return fibo(n-1) + fibo(n-2)

print(fibo(6))
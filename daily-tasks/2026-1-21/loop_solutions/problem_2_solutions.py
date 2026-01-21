# Loop Problem 2:
# Write a program to print the fibonacci series upto nth term.

n = 5
fibo = [0, 1]

for i in range(2, n):
    fibo.append(fibo[i-1] + fibo[i-2])

print(fibo)


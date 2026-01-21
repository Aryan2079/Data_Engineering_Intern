# Function problem 2:
# Write a function that takes a list of numbers and returns the maximum value without using Python’s built-in max().

def max_val(arr):
    max = arr[0]

    for i in arr:
        if i > max:
            max = i

    return max

print(max_val([1,2,3,4,5]))
# List problem 1: Write a function that takes a list of integers as input and returns a new list where each element is the product of all the other elements in the list (except for itself). For example, given the list [1, 2, 3, 4], the function should return [24, 12, 8, 6].
# -- list comprehension + for loop problem

from math import prod

def foo(arr):
    output = [prod([arr[j] for j in range(len(arr)) if i != j]) for i in range(len(arr))]
    print(output)

foo([1,2,3,4]) 
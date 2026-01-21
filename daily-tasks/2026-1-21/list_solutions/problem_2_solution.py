# List problem 2: Write a function that takes two lists as input and returns a new list containing the elements that are common to both lists.
# Example: 
# a = [1, 2, 3, 4, 5]
# b = [4, 5, 6, 7, 8]
# common_list = [4, 5]

a = [1, 2, 3, 4, 5]
b = [4, 5, 6, 7, 8]

def foo(arr1, arr2):
    output = [i for i in arr1 if i in arr2]
    print(output)

foo(a,b)
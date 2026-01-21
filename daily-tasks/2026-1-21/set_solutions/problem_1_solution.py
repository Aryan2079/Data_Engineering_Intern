# Set problem 1: Write a function that takes two lists as input and returns a new set containing the elements that are in the first list but not in the second list.
# Example:
# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7, 8]
# Output: {1, 2, 3}

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

def foo(arr1, arr2):
    output = {i for i in arr1 if i not in arr2}
    return output

print(foo(list1, list2))

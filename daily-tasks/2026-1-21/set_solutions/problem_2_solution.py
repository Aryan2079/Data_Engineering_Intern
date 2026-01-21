# Set problem 2: Write a function that takes a list of strings as input and returns a new set containing all the unique characters in all the strings.
# Example:
# strings = ['hello', 'world', '']
# Output: {'d', 'e', 'h', 'l', 'n', 'o', 'p', 'r', 't', 'w', 'y'}

strings = ['hello', 'world', '']
def foo(arr):

    output = {j for i in arr for j in i}
    return output

print(foo(strings))
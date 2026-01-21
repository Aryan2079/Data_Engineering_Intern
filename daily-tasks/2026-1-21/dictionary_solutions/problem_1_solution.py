# Dictionary problem 1: Write a function that takes a list of dictionaries as input, where each dictionary represents a person with keys 'name' and 'age', and returns a new dictionary where the keys are the ages and the values are lists of names that correspond to that age.
# people = [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}, {'name': 'Charlie', 'age': 25}]
# # Output: {25: ['Alice', 'Charlie'], 30: ['Bob']}

def foo(arr):
    output = {}

    for person in arr:
        output.setdefault(person["age"], []).append(person["name"])

    print(output)

foo([{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}, {'name': 'Charlie', 'age': 25}])
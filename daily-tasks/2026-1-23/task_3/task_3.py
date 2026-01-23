# task 3: Use a with statement to open a file and print all its contents.

with open("test.txt", 'r') as f:
    contents =  f.read()
    print(contents)
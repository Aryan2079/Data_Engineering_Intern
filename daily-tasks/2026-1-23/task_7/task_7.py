# task 7: Write a Python script to read a CSV file and print its contents row by row.

def read_csv(file_path):
    with open(file_path, 'r') as f:
        for line_n, line in enumerate(f.readlines()):
            print(f"row-{line_n+1}: {line}")

read_csv("test.csv")
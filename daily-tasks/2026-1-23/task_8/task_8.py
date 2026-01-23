# problem 8: Write a program to create a CSV file with columns: id, name, age, and insert 3 rows of data.

class CSV:
    def __init__(self, file_path, columns):
        self.columns = columns
        self.file_path = file_path

        with open(self.file_path, 'w', encoding='utf-8') as f:
            f.write(",".join([column.strip() for column in self.columns]) + "\n")

    def insert_data(self, data):
        if len(data) != len(self.columns):
            raise ValueError("the number of data entries doesn't match the number of columns")

        with open(self.file_path, 'a', encoding='utf-8') as f:
            f.write(",".join([str(entry).strip() for entry in data]) + "\n")


csv = CSV('test.csv', ['id', 'name', 'age'])
csv.insert_data(['1', 'aryan', 22])
csv.insert_data(['2', 'kafle', 21])
csv.insert_data(['3', 'bigyan', 25])


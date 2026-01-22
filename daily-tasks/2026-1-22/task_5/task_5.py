# Task 5: Write a class DataSize with init, str, and add so you can add two DataSize objects and print them nicely.

class DataSize:
    def __init__(self, data_name, size):
        self.data_name = data_name
        self.size = size

    def __add__(self, other):
        if isinstance(other, DataSize):
            return DataSize(f"{self.data_name}+{other.data_name}", self.size + other.size)
        else:
            raise TypeError("Can only add DataSize with DataSize")
        
    def __str__(self):
        return f"{self.size} bytes"
    
file1 = DataSize("abc", 1500)       #1500 bytes
file2 = DataSize("def", 2500)      # 2500 bytes

total = file1 + file2

print(f"{file1.data_name}: {file1.size}")  
print(f"{file2.data_name}: {file2.size}")   
print(f"{total.data_name}: {total.size}")   


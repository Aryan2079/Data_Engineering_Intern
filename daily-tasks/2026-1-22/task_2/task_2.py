# Task 2: Write a Laptop class with attributes brand and price. Create 3 objects and store them in a list. Print the list in a readable way (e.g., Dell - $800).

class Laptop:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

dell = Laptop("dell", 90000)
lenevo = Laptop("lenevo", 100000)
mac = Laptop("dell", 200000)

laptop_list = [dell, lenevo, mac]

for laptop in laptop_list:
    print(f"{laptop.brand} - {laptop.price}")
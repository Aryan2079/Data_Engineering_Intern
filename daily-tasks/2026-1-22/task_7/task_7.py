# Task 7: Create a class Dog with a class variable species = "Canine". Each object should also have its own name. Demonstrate the difference by printing both.

class Dog:
    species = "Canine"
    
    def __init__(self, name):
        self.name = name

dog1 = Dog('kali')
dog2 = Dog('gufy')

print(dog1.name)  
print(dog2.name)  

print(dog1.species) 
print(dog2.species) 

print(Dog.species)  
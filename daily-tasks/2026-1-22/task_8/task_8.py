# Task 8: Extend the Dog class with a counter (class variable) that tracks how many dogs have been created so far.

class Dog:
    species = "Canine"
    
    def __init__(self, name):
        self.name = name

class DogCounter(Dog):
    count = 0

    def __init__(self, name):
        super().__init__(name)
        DogCounter.count += 1

d1 = DogCounter("kali")
d2 = DogCounter("gufy")

print(f"The number of dogs created: {DogCounter.count}")

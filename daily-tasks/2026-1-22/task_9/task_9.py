# Task 9: Create a class MathOps with:
        
# an instance method square(self, x)
# a classmethod cube(cls, x)
# a staticmethod is_even(x)

class MathOps:
    def square(self, x):
        return x*x
    
    @classmethod
    def cube(cls, x):
        return x**3
    
    @staticmethod
    def is_even(x):
        return x%2==0
    
print(MathOps().square(2))
print(MathOps.cube(2))
print(MathOps.is_even(2))
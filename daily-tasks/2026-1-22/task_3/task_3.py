# Task 3: Create an abstract base class Employee (use ABC) with:
    # Abstract method calculate_salary()
    # Abstract method get_role()
    # Concrete method display_info() that uses the abstract methods
    # Class variable company_name

# Create inheritance hierarchy:
# Employee
# ├── FullTimeEmployee (has annual_salary, benefits)
# │   └── Manager (has team_size, bonus_percentage)
# │       └── Director (has department, additional_stock_options)
# └── ContractEmployee (has hourly_rate, hours_worked, contract_duration)

# Each subclass must:
    # Implement all abstract methods differently
    # Override work() method with specific behavior
    # Call parent's init using super()
    # Add at least one unique method

# Demonstrate:
    # Polymorphism: store different employee types in a list and call methods
    # Method resolution order (MRO) by printing it
    # Creating instances of all concrete classes (not abstract Employee)
    # Show how each calculates salary differently

from abc import ABC, abstractmethod
from enum import Enum, auto

class Roles(Enum):
    Manager = auto()
    Director = auto()
    ContractEmployee = auto()
    FullTimeEmployee = auto()

class Employee(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def calculate_salary(self):
        pass

    @abstractmethod
    def get_role(self):
        pass

    @abstractmethod
    def work(self):
        pass

    def display_info(self):
        print(f"Name:{self.name} Role: {self.get_role()}, Salary is: {self.calculate_salary()}")

class FullTimeEmployee(Employee):
    def __init__(self, name, annual_salary, benefits):
        super().__init__(name)
        self.annual_salary = annual_salary
        self.benefits = benefits

    def calculate_salary(self):
        return self.annual_salary

    def get_role(self):
        return Roles.FullTimeEmployee.name
    
    def work(self):
        print("I work 9 hours a day")

    def list_benefits(self):
        return f"Benefits:, {''.join(self.benefits)}"


class Manager(FullTimeEmployee):
    def __init__(self, name, annual_salary, benefits, team_size, bonus_percentage):
        super().__init__(name, annual_salary, benefits)
        self.team_size = team_size
        self.bonus_percentage = bonus_percentage

    def calculate_salary(self):
        bonus = self.annual_salary * self.bonus_percentage
        return self.annual_salary + bonus

    def get_role(self):
        return Roles.Manager.name

    def work(self):
        print("I work 5 hours a day")

    def conduct_meeting(self):
        return f"Conducting meetings for a team of {self.team_size} members."


class Director(Manager):
    def __init__(self, name, annual_salary, benefits, team_size, bonus_percentage, department, additional_stock_options):
        super().__init__(name, annual_salary, benefits, team_size, bonus_percentage)
        self.department = department
        self.additional_stock_options = additional_stock_options
    
    def calculate_salary(self):
        base_salary_with_bonus = super().calculate_salary()
        return base_salary_with_bonus + self.additional_stock_options

    def get_role(self):
        return Roles.Director.name

    def work(self):
        print("I work 3 hours a day")

    def approve_budget(self):
        return f"Budget approved for {self.department} department."


class ContractEmployee(Employee):
    def __init__(self, name, hourly_rate, hours_worked, contract_duration):
        super().__init__(name)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
        self.contract_duraction = contract_duration

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked

    def get_role(self):
        return Roles.ContractEmployee.name

    def work(self):
        print("I work somedays")

    def extend_contract(self, extra_months):
        self.contract_duration += extra_months
        return f"Contract extended to {self.contract_duration} months."


emp1 = FullTimeEmployee(
    "Bigyan",
    annual_salary=10000,
    benefits=["Health insurance", "Transportation"]
)

emp2 = Manager(
        "Kafle",
        annual_salary=80000,
        benefits=["Health Insurance", "Transportation", "Paid Leave"],
        team_size=8,
        bonus_percentage=0.15
    )

emp3 = Director(
        "Aryan",
        annual_salary=100000,
        benefits=["Health Insurance", "Transportation", "Stock Plan"],
        team_size=20,
        bonus_percentage=0.25,
        department="Engineering",
        additional_stock_options=20000
    )

emp4 = ContractEmployee(
        "Ram",
        hourly_rate=50,
        hours_worked=160,
        contract_duration=6
    )

employees = [emp1, emp2, emp3, emp4]

# demonstrate polymorphism
for emp in employees:
    emp.display_info()
    emp.work()

# print mro
for cls in Director.__mro__:
    print(cls)

# printing salaries
print(f"{emp1.name}: {emp1.calculate_salary()} (Annual)")
print(f"{emp2.name}: {emp2.calculate_salary()} (Annual + Bonus)")
print(f"{emp3.name}: {emp3.calculate_salary()} (Annual + Bonus + Stock)")
print(f"{emp4.name}: {emp4.calculate_salary()} (Hourly × Hours)")
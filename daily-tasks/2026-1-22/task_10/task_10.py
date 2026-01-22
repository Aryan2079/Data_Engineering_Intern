# Task 10: 
#  Create an Employee class with class variable company = "GrowByData"
# Implement a classmethod to change company name with validation:
   
# Must be 3-50 characters
# Must contain only letters, numbers, and spaces
# Add instance attributes: name, email, employee_id, salary, department
# Implement a classmethod to generate unique employee IDs (format: EMP-YYYY-XXXX)
# Add a class variable to track all employees and department counts

from datetime import datetime
import regex as re

class Employee:
    company = "GrowByData"
    employees = []
    department_count = {}
    _id_counter = 0

    def __init__(self, name, email, employee_id, salary, department):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary
        self.department = department
        self.email = email
        Employee.employees.append(self)
        Employee.department_count[department] = Employee.department_count.get(department, 0) + 1

    @classmethod
    def generate_employee_id(cls):
        year = datetime.now().year
        cls._id_counter += 1
        return f"EMP-{year}-{cls._id_counter:04d}"

    @classmethod
    def change_company_name(cls, new_name):
        if not (3 <= len(new_name) <= 50):
            raise ValueError("Name must be between 3 and 50 characters")
        if not re.match(r"^[A-Za-z0-9 ]+$", new_name):
            raise ValueError("Name can only contain letters, numbers, and spaces")
        cls.company = new_name
        
    def __str__(self):
        return (f"{self.name} | {self.email} | ID: {self.employee_id} | "
                f"Salary: {self.salary} | Dept: {self.department}")
    

e1 = Employee("Aryan Bhattarai", Employee.generate_employee_id() , "aryan@example.com", 60000, "Engineering")
e2 = Employee("Aady Kafle",Employee.generate_employee_id(), "kafle@example.com", 55000, "Engineering")
e3 = Employee("Bigyan Moktan",Employee.generate_employee_id(), "bigyan@example.com", 70000, "HR")

print(e1)
print(e2)
print(e3)

print(Employee.department_count)  

print([emp.employee_id for emp in Employee.employees])

Employee.change_company_name("grow by protein")
print(Employee.company)
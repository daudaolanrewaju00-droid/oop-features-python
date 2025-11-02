# imam.py

# Base class (Encapsulation)
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_info(self):
        print(f"Employee Name: {self.name}")
        print(f"Salary: ₦{self.salary}")

# Inheritance
class Manager(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)  # inherit from Employee

    # Polymorphism (method overriding)
    def calculate_bonus(self):
        return self.salary * 0.2

# Another subclass
class Developer(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)

    def calculate_bonus(self):
        return self.salary * 0.1

# Abstraction via simple interface (demonstration)
def show_bonus(employee):
    print(f"{employee.name}'s Bonus: ₦{employee.calculate_bonus()}")

# Testing the integration
employees = [
    Manager("Aregbe", 100000),
    Developer("Mimi", 80000)
]

for emp in employees:
    emp.display_info()
    show_bonus(emp)
    print("-" * 40)

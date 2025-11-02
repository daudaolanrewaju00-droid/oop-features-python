from abc import ABC, abstractmethod

# Abstraction and Encapsulation
class Employee(ABC):
    def _init_(self, name, salary):
        self.name = name
        self.__salary = salary  # Encapsulation (private attribute)

    @abstractmethod
    def calculate_bonus(self):
        pass  # Abstraction

    def get_salary(self):
        return self.__salary


# Inheritance and Polymorphism
class Manager(Employee):
    def calculate_bonus(self):
        return self.get_salary() * 0.20  # Polymorphism


class Developer(Employee):
    def calculate_bonus(self):
        return self.get_salary() * 0.10  # Polymorphism


# Creating objects and using them
employees = [
    Manager("Aregbe", 100000),
    Developer("Mimi", 80000)
]

for emp in employees:
    print(f"{emp.name}'s Bonus: ₦{emp.calculate_bonus()}")

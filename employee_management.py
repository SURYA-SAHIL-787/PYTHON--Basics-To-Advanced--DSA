from abc import ABC, abstractmethod

class Employee(ABC):
    employee_count = 0

    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary
        Employee.employee_count += 1

    def get_salary(self):
        return self.__salary

    @abstractmethod
    def show_role(self):
        pass

class Manager(Employee):
    def show_role(self):
        return f"{self.name} is a Manager with salary {self.get_salary()}"

class Developer(Employee):
    def show_role(self):
        return f"{self.name} is a Developer with salary {self.get_salary()}"

class Tester(Employee):
    def show_role(self):
        return f"{self.name} is a Tester with salary {self.get_salary()}"

employees = [Manager("Sahil", 80000), Developer("Raj", 60000), Tester("Anu", 50000)]

for emp in employees:
    print(emp.show_role())

print("Total Employees:", Employee.employee_count)

class Employee:
    def __init__(self, emp_id, name, base_salary):
        self.emp_id = emp_id
        self.name = name
        self.base_salary = base_salary

    def calculate_salary(self):
        return self.base_salary

    def display(self):
        print(f"ID: {self.emp_id}, Name: {self.name}, Salary: {self.calculate_salary()}")


class Manager(Employee):
    def __init__(self, emp_id, name, base_salary, bonus):
        super().__init__(emp_id, name, base_salary)
        self.bonus = bonus

    def calculate_salary(self):
        return self.base_salary + self.bonus


class Developer(Employee):
    def __init__(self, emp_id, name, base_salary, overtime_hours, overtime_rate):
        super().__init__(emp_id, name, base_salary)
        self.overtime_hours = overtime_hours
        self.overtime_rate = overtime_rate

    def calculate_salary(self):
        return self.base_salary + (self.overtime_hours * self.overtime_rate)


class Intern(Employee):
    def __init__(self, emp_id, name, stipend):
        super().__init__(emp_id, name, stipend)

    def calculate_salary(self):
        return self.base_salary


employees = [
    Manager(1, "Anil", 70000, 15000),
    Developer(2, "Sahil", 50000, 20, 500),
    Intern(3, "Ravi", 15000)
]

for emp in employees:
    emp.display()

from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, emp_id, name):
        self.emp_id = emp_id
        self.name = name

    @abstractmethod
    def calculate_salary(self):
        pass

    def __str__(self):
        return f"Employee ID: {self.emp_id}, Name: {self.name}"


class FullTimeEmployee(Employee):
    def __init__(self, emp_id, name, monthly_salary, bonus=0):
        super().__init__(emp_id, name)
        self.monthly_salary = monthly_salary
        self.bonus = bonus

    def calculate_salary(self):
        return self.monthly_salary + self.bonus


class PartTimeEmployee(Employee):
    def __init__(self, emp_id, name, hourly_rate, hours_worked):
        super().__init__(emp_id, name)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked


class ContractEmployee(Employee):
    def __init__(self, emp_id, name, contract_amount):
        super().__init__(emp_id, name)
        self.contract_amount = contract_amount

    def calculate_salary(self):
        return self.contract_amount


class PayrollSystem:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        if not isinstance(employee, Employee):
            raise TypeError("Only Employee objects can be added.")
        self.employees.append(employee)

    def generate_payroll(self):
        print("Payroll Report")
        print("-" * 40)
        total_payroll = 0

        for emp in self.employees:
            salary = emp.calculate_salary()
            total_payroll += salary
            print(f"{emp.name} ({emp.emp_id}) --> Salary: {salary}")

        print("-" * 40)
        print(f"Total Payroll Expense: {total_payroll}")


# Example usage
if __name__ == "__main__":
    e1 = FullTimeEmployee(1, "Sahil", 50000, 5000)
    e2 = PartTimeEmployee(2, "Ravi", 500, 60)
    e3 = ContractEmployee(3, "Meena", 40000)

    payroll = PayrollSystem()
    payroll.add_employee(e1)
    payroll.add_employee(e2)
    payroll.add_employee(e3)

    payroll.generate_payroll()

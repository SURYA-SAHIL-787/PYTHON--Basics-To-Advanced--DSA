class Employee:
    def __init__(self, name, salaries):
        self.name = name
        self.salaries = salaries

    def total_salary(self):
        return sum(self.salaries)

    def highest_salary(self):
        return max(self.salaries)


try:
    name = input("Enter employee name: ")
    salaries = []

    n = int(input("Enter number of months: "))

    for i in range(n):
        salary = float(input(f"Enter salary for month {i+1}: "))

        if salary < 0:
            raise ValueError("Salary cannot be negative")

        salaries.append(salary)

    emp = Employee(name, salaries)

    print("Employee Name:", emp.name)
    print("Salary Array:", emp.salaries)
    print("Total Salary:", emp.total_salary())
    print("Highest Salary:", emp.highest_salary())

except ValueError as e:
    print("Error:", e)

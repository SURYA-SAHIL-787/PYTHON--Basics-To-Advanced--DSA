from abc import ABC, abstractmethod

class Staff(ABC):
    staff_count = 0

    def __init__(self, name, department):
        self.name = name
        self.__department = department
        Staff.staff_count += 1

    def get_department(self):
        return self.__department

    @abstractmethod
    def role(self):
        pass

class Doctor(Staff):
    def role(self):
        return f"Dr. {self.name} works in {self.get_department()} department"

class Nurse(Staff):
    def role(self):
        return f"Nurse {self.name} works in {self.get_department()} department"

class Receptionist(Staff):
    def role(self):
        return f"Receptionist {self.name} works in {self.get_department()} department"

staff_members = [Doctor("Arun", "Cardiology"), Nurse("Meena", "ICU"), Receptionist("Riya", "Front Desk")]

for member in staff_members:
    print(member.role())

print("Total Staff:", Staff.staff_count)

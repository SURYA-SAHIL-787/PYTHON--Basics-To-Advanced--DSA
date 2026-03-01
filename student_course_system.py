from abc import ABC, abstractmethod

class Student(ABC):
    student_count = 0

    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks
        Student.student_count += 1

    def get_marks(self):
        return self.__marks

    @abstractmethod
    def course(self):
        pass

class CSEStudent(Student):
    def course(self):
        return f"{self.name} is a CSE student with marks {self.get_marks()}"

class ECEStudent(Student):
    def course(self):
        return f"{self.name} is an ECE student with marks {self.get_marks()}"

class MEStudent(Student):
    def course(self):
        return f"{self.name} is a Mechanical student with marks {self.get_marks()}"

students = [CSEStudent("Sahil", 91), ECEStudent("Kiran", 88), MEStudent("Varun", 84)]

for s in students:
    print(s.course())

print("Total Students:", Student.student_count)

from abc import ABC, abstractmethod

class Student:
    def __init__(self, roll_no, name):
        self.roll_no = roll_no
        self.name = name
        self.marks = {}

    def add_marks(self, subject, marks):
        self.marks[subject] = marks

    def display_marks(self):
        print(f"Marks of {self.name}:")
        for subject, marks in self.marks.items():
            print(subject, ":", marks)


class ResultProcessor(ABC):
    @abstractmethod
    def calculate_result(self, student):
        pass


class GradeResultProcessor(ResultProcessor):
    def calculate_result(self, student):
        average = sum(student.marks.values()) / len(student.marks)
        if average >= 90:
            return "A"
        elif average >= 75:
            return "B"
        elif average >= 50:
            return "C"
        else:
            return "Fail"


class CGPAResultProcessor(ResultProcessor):
    def calculate_result(self, student):
        average = sum(student.marks.values()) / len(student.marks)
        return round(average / 10, 2)


# Driver Code
s1 = Student(101, "Sahil")
s1.add_marks("Math", 95)
s1.add_marks("Python", 88)
s1.add_marks("DSA", 91)

grade_processor = GradeResultProcessor()
cgpa_processor = CGPAResultProcessor()

s1.display_marks()
print("Grade:", grade_processor.calculate_result(s1))
print("CGPA:", cgpa_processor.calculate_result(s1))

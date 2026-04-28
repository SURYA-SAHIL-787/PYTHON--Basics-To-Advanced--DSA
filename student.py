class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def total_marks(self):
        return sum(self.marks)

    def average_marks(self):
        return self.total_marks() / len(self.marks)


try:
    name = input("Enter student name: ")
    marks = []

    for i in range(5):
        mark = int(input(f"Enter mark {i+1}: "))
        if mark < 0 or mark > 100:
            raise ValueError("Marks must be between 0 and 100")
        marks.append(mark)

    student = Student(name, marks)

    print("Student Name:", student.name)
    print("Marks:", student.marks)
    print("Total Marks:", student.total_marks())
    print("Average Marks:", student.average_marks())

except ValueError as e:
    print("Error:", e)

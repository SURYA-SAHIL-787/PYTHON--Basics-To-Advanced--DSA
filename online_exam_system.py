from abc import ABC, abstractmethod


class Question(ABC):
    def __init__(self, question_id, text, marks):
        self.question_id = question_id
        self.text = text
        self.marks = marks

    @abstractmethod
    def evaluate(self, answer):
        pass

    @abstractmethod
    def display(self):
        pass


class MultipleChoiceQuestion(Question):
    def __init__(self, question_id, text, options, correct_option, marks):
        super().__init__(question_id, text, marks)
        self.options = options
        self.correct_option = correct_option

    def evaluate(self, answer):
        return self.marks if answer.strip().upper() == self.correct_option.upper() else 0

    def display(self):
        print(f"Q{self.question_id}: {self.text}")
        for key, value in self.options.items():
            print(f"  {key}. {value}")


class TrueFalseQuestion(Question):
    def __init__(self, question_id, text, correct_answer, marks):
        super().__init__(question_id, text, marks)
        self.correct_answer = correct_answer

    def evaluate(self, answer):
        return self.marks if answer.strip().lower() == str(self.correct_answer).lower() else 0

    def display(self):
        print(f"Q{self.question_id}: {self.text} (True/False)")


class DescriptiveQuestion(Question):
    def __init__(self, question_id, text, keywords, marks):
        super().__init__(question_id, text, marks)
        self.keywords = keywords

    def evaluate(self, answer):
        answer = answer.lower()
        matched = sum(1 for word in self.keywords if word.lower() in answer)
        return (matched / len(self.keywords)) * self.marks

    def display(self):
        print(f"Q{self.question_id}: {self.text} (Descriptive)")


class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.answers = {}

    def submit_answer(self, question_id, answer):
        self.answers[question_id] = answer


class Exam:
    def __init__(self, title):
        self.title = title
        self.questions = []

    def add_question(self, question):
        self.questions.append(question)

    def conduct_exam(self, student):
        print(f"\nExam: {self.title}")
        total_score = 0
        max_score = 0

        for question in self.questions:
            question.display()
            answer = student.answers.get(question.question_id, "")
            score = question.evaluate(answer)
            total_score += score
            max_score += question.marks
            print(f"Answer: {answer}")
            print(f"Score: {score}/{question.marks}\n")

        print(f"Final Score of {student.name}: {total_score}/{max_score}")


if __name__ == "__main__":
    exam = Exam("Python OOP Test")

    q1 = MultipleChoiceQuestion(
        1,
        "Which keyword is used to create a class in Python?",
        {"A": "function", "B": "class", "C": "define", "D": "object"},
        "B",
        5
    )
    q2 = TrueFalseQuestion(2, "Python supports multiple inheritance.", True, 5)
    q3 = DescriptiveQuestion(3, "What is encapsulation?", ["data", "methods", "hide"], 10)

    exam.add_question(q1)
    exam.add_question(q2)
    exam.add_question(q3)

    student = Student(101, "Sahil")
    student.submit_answer(1, "B")
    student.submit_answer(2, "True")
    student.submit_answer(3, "Encapsulation hides data and methods inside a class.")

    exam.conduct_exam(student)

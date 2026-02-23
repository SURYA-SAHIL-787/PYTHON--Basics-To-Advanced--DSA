class A:
    def __init__(self):
        print("A init")
        super().__init__()
    def work(self):
        return "A work"

class B:
    def __init__(self):
        print("B init")
        super().__init__()
    def work(self):
        return "B work"

class C(A, B):
    def __init__(self):
        print("C init")
        super().__init__()   # follows MRO: C -> A -> B -> object
    def work(self):
        return super().work() + " -> C extra"

obj = C()
print("Work:", obj.work())
print("MRO:", [cls.__name__ for cls in C.mro()])

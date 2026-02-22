def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b): return a / b if b != 0 else "Cannot divide by zero"

a = float(input("Enter a: "))
b = float(input("Enter b: "))
op = input("Enter operator (+ - * /): ")

if op == "+": print(add(a, b))
elif op == "-": print(sub(a, b))
elif op == "*": print(mul(a, b))
elif op == "/": print(div(a, b))
else: print("Invalid operator")

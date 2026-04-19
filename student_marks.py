marks = {
    "Sahil": 95,
    "Rahul": 88,
    "Anita": 92
}

print("Original marks:", marks)

marks["Priya"] = 90
marks["Rahul"] = 91

print("Updated marks:", marks)

name = "Sahil"
if name in marks:
    print(name, "marks =", marks[name])
else:
    print(name, "not found")

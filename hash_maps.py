# Hash Maps in Python

# Creating a hash map
student_marks = {
    "Sahil": 95,
    "Rahul": 88,
    "Anita": 92
}

# Accessing values
print("Marks of Sahil:", student_marks["Sahil"])

# Adding a new key-value pair
student_marks["Priya"] = 90
print("After adding Priya:", student_marks)

# Updating a value
student_marks["Rahul"] = 91
print("After updating Rahul:", student_marks)

# Removing a key-value pair
del student_marks["Anita"]
print("After deleting Anita:", student_marks)

# Checking if a key exists
if "Priya" in student_marks:
    print("Priya is present in the hash map")

# Iterating through hash map
print("All students and marks:")
for key, value in student_marks.items():
    print(key, ":", value)

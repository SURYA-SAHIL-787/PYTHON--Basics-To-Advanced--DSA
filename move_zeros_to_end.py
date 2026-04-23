arr = [4, 0, 7, 0, 1, 9, 0, 3]

result = []

for num in arr:
    if num != 0:
        result.append(num)

while len(result) < len(arr):
    result.append(0)

print("Array after moving zeros to end:", result)

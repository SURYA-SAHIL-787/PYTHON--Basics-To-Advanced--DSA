arr = [4, 5, 2, 25, 7, 8]

result = []

for i in range(len(arr)):
    next_greater = -1

    for j in range(i + 1, len(arr)):
        if arr[j] > arr[i]:
            next_greater = arr[j]
            break

    result.append(next_greater)

print("Original array:", arr)
print("Next greater array:", result)

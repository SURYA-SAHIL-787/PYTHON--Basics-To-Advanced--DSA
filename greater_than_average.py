arr = [10, 20, 30, 40, 50, 15, 25]

average = sum(arr) / len(arr)
count = 0

for num in arr:
    if num > average:
        count += 1

print("Average:", average)
print("Elements greater than average:", count)

arr = [10, 22, 28, 29, 30, 40]
target = 54

closest_pair = None
smallest_difference = float("inf")

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        pair_sum = arr[i] + arr[j]
        difference = abs(target - pair_sum)

        if difference < smallest_difference:
            smallest_difference = difference
            closest_pair = (arr[i], arr[j])

print("Pair with sum closest to target:", closest_pair)
print("Closest sum:", sum(closest_pair))

def count_frequency(arr):
    freq = {}

    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    return freq


# Example usage
arr = [1, 2, 2, 3, 1, 4, 2, 3]
result = count_frequency(arr)

print("Element frequencies:")
for key, value in result.items():
    print(f"{key} -> {value}")

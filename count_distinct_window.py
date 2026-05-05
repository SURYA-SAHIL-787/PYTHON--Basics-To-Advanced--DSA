def count_distinct(arr, k):
    freq = {}
    result = []

    for i in range(len(arr)):
        freq[arr[i]] = freq.get(arr[i], 0) + 1

        if i >= k:
            left = arr[i - k]
            freq[left] -= 1
            if freq[left] == 0:
                del freq[left]

        if i >= k - 1:
            result.append(len(freq))

    return result


arr = [1, 2, 1, 3, 4, 2, 3]
k = 4

print(count_distinct(arr, k))

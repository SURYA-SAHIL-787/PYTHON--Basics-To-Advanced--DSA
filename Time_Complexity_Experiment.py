# Write a Python program that:
# 1. Generates random arrays of sizes:
#    - 100
#    - 500
#    - 1000
# 2. Sorts them using Bubble Sort.
# 3. Measures and prints the execution time for each case.
# Use Python's time module.

import random
import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

sizes = [100, 500, 1000]

for size in sizes:
    arr = [random.randint(1, 1000) for _ in range(size)]

    start_time = time.time()
    bubble_sort(arr)
    end_time = time.time()

    execution_time = end_time - start_time

    print("Array size:", size)
    print("Execution time:", execution_time, "seconds")
    print()

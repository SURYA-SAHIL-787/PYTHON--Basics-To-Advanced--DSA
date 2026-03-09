# Write a Python program that:
# 1. Accepts n numbers.
# 2. Sorts the numbers using:
#    - Bubble Sort
#    - Insertion Sort
# 3. Displays both sorted arrays.
# Also count and print the number of comparisons performed by each algorithm.

def bubble_sort(arr):
    comparisons = 0
    a = arr.copy()

    for i in range(len(a)):
        for j in range(0, len(a) - i - 1):
            comparisons += 1
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]

    return a, comparisons


def insertion_sort(arr):
    comparisons = 0
    a = arr.copy()

    for i in range(1, len(a)):
        key = a[i]
        j = i - 1

        while j >= 0:
            comparisons += 1
            if a[j] > key:
                a[j + 1] = a[j]
                j -= 1
            else:
                break

        a[j + 1] = key

    return a, comparisons


n = int(input("Enter number of elements: "))

arr = []
for i in range(n):
    value = int(input(f"Enter element {i + 1}: "))
    arr.append(value)

bubble_sorted, bubble_comp = bubble_sort(arr)
insertion_sorted, insertion_comp = insertion_sort(arr)

print("Bubble Sort Result:", bubble_sorted)
print("Bubble Sort Comparisons:", bubble_comp)

print("Insertion Sort Result:", insertion_sorted)
print("Insertion Sort Comparisons:", insertion_comp)

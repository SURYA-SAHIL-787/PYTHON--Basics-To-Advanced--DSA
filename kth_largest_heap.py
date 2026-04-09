import heapq

def find_kth_largest(arr, k):
    min_heap = []

    for num in arr:
        heapq.heappush(min_heap, num)
        if len(min_heap) > k:
            heapq.heappop(min_heap)

    return min_heap[0]

arr = [7, 10, 4, 3, 20, 15]
k = 3

print("Kth Largest Element:", find_kth_largest(arr, k))

import heapq

heap = []

heapq.heappush(heap, 20)
heapq.heappush(heap, 5)
heapq.heappush(heap, 15)
heapq.heappush(heap, 22)
heapq.heappush(heap, 9)

print("Min Heap After Insertions:", heap)

smallest = heapq.heappop(heap)
print("Deleted Smallest Element:", smallest)

print("Min Heap After Deletion:", heap)

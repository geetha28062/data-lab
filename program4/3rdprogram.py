import heapq

heap = []

heapq.heappush(heap, 30)
heapq.heappush(heap, 10)
heapq.heappush(heap, 20)
heapq.heappush(heap, 5)

print("Min Heap:", heap)

x = heapq.heappop(heap)
print("Deleted:", x)

print("After deletion:", heap)
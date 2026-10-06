import heapq

arr = [40, 10, 30, 20, 50]

heap = []

for x in arr:
    heapq.heappush(heap, x)

sorted_list = []

while heap:
    sorted_list.append(heapq.heappop(heap))

print("Original:", arr)
print("Sorted:", sorted_list)
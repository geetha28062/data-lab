queue = []

n = int(input("Enter number of elements: "))

for i in range(n):
    x = int(input("Enter element: "))
    queue.append(x)

print("Queue:", queue)

if queue:
    print("Deleted:", queue.pop(0))

print("Queue after deletion:", queue)
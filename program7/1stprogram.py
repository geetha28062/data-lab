n = int(input("Enter number of items: "))

items = []
for i in range(n):
    w = int(input("Enter weight: "))
    v = int(input("Enter value: "))
    items.append((v / w, w, v))

capacity = int(input("Enter capacity: "))

items.sort(reverse=True)
profit = 0

for ratio, weight, value in items:
    if capacity >= weight:
        capacity -= weight
        profit += value
    else:
        profit += ratio * capacity
        break

print("Maximum Profit:", profit)
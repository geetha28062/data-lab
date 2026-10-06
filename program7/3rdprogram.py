n = int(input("Enter number of items: "))
items = []

for i in range(n):
    w = int(input("Weight: "))
    v = int(input("Value: "))
    items.append([v / w, w, v, i + 1])

c = int(input("Enter capacity: "))
items.sort(reverse=True)

profit = 0

for ratio, weight, value, item in items:
    if c == 0:
        break

    take = min(weight, c)
    profit += take * ratio
    c -= take

    print("Item", item, "taken:", take)

print("Maximum Profit:", profit)
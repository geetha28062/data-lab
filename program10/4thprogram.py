def branch(cost, driver, used, total, path):
    global best_cost, best_path

    if driver == len(cost):
        if total < best_cost:
            best_cost = total
            best_path = path[:]
        return

    for route in range(len(cost)):
        if route not in used:
            used.add(route)

            branch(cost, driver + 1, used,
                   total + cost[driver][route],
                   path + [route])

            used.remove(route)


cost = [
    [10, 5, 8],
    [7, 6, 4],
    [3, 9, 5]
]

best_cost = 9999
best_path = []

branch(cost, 0, set(), 0, [])

print("Minimum Travel Cost:", best_cost)

for i, route in enumerate(best_path):
    print("Driver", i + 1, "-> Route", route + 1)
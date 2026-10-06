def assign(cost, employee, used, path, total, best):
    n = len(cost)

    if employee == n:
        if total < best[0]:
            best[0] = total
            best[1] = path[:]
        return

    for job in range(n):
        if not used[job]:
            used[job] = True

            assign(cost, employee + 1,
                   used,
                   path + [job],
                   total + cost[employee][job],
                   best)

            used[job] = False


employees = ["A", "B", "C"]
jobs = ["Coding", "Testing", "Design"]

cost = [
    [9, 2, 7],
    [6, 4, 3],
    [5, 8, 1]
]

best = [9999, []]

assign(cost, 0, [False] * 3,
       [], 0, best)

print("Minimum Cost:", best[0])

for i, j in enumerate(best[1]):
    print(employees[i], "->", jobs[j])
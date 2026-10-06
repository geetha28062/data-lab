def branch(cost, row, used, total, path, best):
    n = len(cost)

    if row == n:
        if total < best[0]:
            best[0] = total
            best[1] = path[:]
        return

    for job in range(n):
        if job not in used:
            used.add(job)

            branch(cost, row + 1,
                   used,
                   total + cost[row][job],
                   path + [job],
                   best)

            used.remove(job)


cost = [
    [10, 2, 8],
    [6, 5, 3],
    [7, 8, 1]
]

print("Cost Matrix:")

for row in cost:
    print(row)

best = [9999, []]

branch(cost, 0, set(), 0, [], best)

print("\nMinimum Cost:", best[0])

for i, j in enumerate(best[1]):
    print("Employee", i + 1,
          "assigned to Job", j + 1)
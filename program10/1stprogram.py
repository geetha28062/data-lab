def solve(cost, assigned, used, row, total, best):
    n = len(cost)

    if row == n:
        if total < best[0]:
            best[0] = total
            best[1] = assigned[:]
        return

    for job in range(n):
        if not used[job]:
            used[job] = True
            assigned.append(job)

            solve(cost, assigned, used, row + 1,
                  total + cost[row][job], best)

            assigned.pop()
            used[job] = False


n = int(input("Enter number of employees: "))

cost = []
for i in range(n):
    cost.append(list(map(int,
        input("Enter costs: ").split())))

best = [float('inf'), []]

solve(cost, [], [False] * n, 0, 0, best)

print("Minimum Cost:", best[0])
print("Job Allocation:")

for i, job in enumerate(best[1]):
    print("Employee", i + 1, "-> Job", job + 1)
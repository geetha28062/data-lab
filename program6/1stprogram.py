# Prim's Algorithm

n = int(input("Enter number of vertices: "))

graph = []
print("Enter weighted adjacency matrix:")

for i in range(n):
    graph.append(list(map(int, input().split())))

selected = [False] * n
selected[0] = True
edges = 0
cost = 0

print("Minimum Spanning Tree:")

while edges < n - 1:
    minimum = 999
    x = y = 0

    for i in range(n):
        if selected[i]:
            for j in range(n):
                if not selected[j] and graph[i][j] != 0:
                    if graph[i][j] < minimum:
                        minimum = graph[i][j]
                        x, y = i, j

    print(x, "--", y, "=", minimum)
    cost += minimum
    selected[y] = True
    edges += 1

print("Minimum Cost:", cost)
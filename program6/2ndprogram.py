# Prim's Algorithm using Edge List

vertices = int(input("Enter number of vertices: "))
edges = int(input("Enter number of edges: "))

graph = []

for i in range(edges):
    u, v, w = map(int, input(
        "Enter source, destination and weight: ").split())
    graph.append((u, v, w))

visited = [False] * vertices
visited[0] = True
mst = []
cost = 0

for k in range(vertices - 1):
    minimum = 999
    selected = None

    for u, v, w in graph:
        if visited[u] and not visited[v] and w < minimum:
            minimum = w
            selected = (u, v, w)

        if visited[v] and not visited[u] and w < minimum:
            minimum = w
            selected = (v, u, w)

    u, v, w = selected
    visited[v] = True
    mst.append((u, v, w))
    cost += w

print("Minimum Spanning Tree:")

for u, v, w in mst:
    print(u, "--", v, "=", w)

print("Minimum Cost:", cost)
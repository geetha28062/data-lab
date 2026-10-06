# Graph using Adjacency List and DFS

n = int(input("Enter number of vertices: "))
graph = {}

for i in range(n):
    graph[i] = list(map(int, input(
        "Enter adjacent vertices of " + str(i) + ": ").split()))

visited = set()

def dfs(v):
    print(v, end=" ")
    visited.add(v)

    for x in graph[v]:
        if x not in visited:
            dfs(x)

start = int(input("Enter starting vertex: "))

print("DFS Traversal:")
dfs(start)
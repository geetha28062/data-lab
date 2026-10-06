# Graph using Adjacency Matrix and DFS

n = int(input("Enter number of vertices: "))
graph = []

print("Enter adjacency matrix:")
for i in range(n):
    graph.append(list(map(int, input().split())))

start = int(input("Enter starting vertex: "))

visited = [False] * n

def dfs(v):
    print(v, end=" ")
    visited[v] = True

    for i in range(n):
        if graph[v][i] == 1 and not visited[i]:
            dfs(i)

print("DFS Traversal:")
dfs(start)
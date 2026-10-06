# Graph using Adjacency Matrix and BFS

n = int(input("Enter number of vertices: "))
graph = []

print("Enter adjacency matrix:")
for i in range(n):
    graph.append(list(map(int, input().split())))

start = int(input("Enter starting vertex: "))

visited = [False] * n
queue = [start]
visited[start] = True

print("BFS Traversal:")

while queue:
    v = queue.pop(0)
    print(v, end=" ")

    for i in range(n):
        if graph[v][i] == 1 and not visited[i]:
            visited[i] = True
            queue.append(i)
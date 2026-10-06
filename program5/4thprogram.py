# BFS and DFS in a Graph

graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0, 3, 4],
    3: [1, 2, 4],
    4: [2, 3]
}

def bfs(start):
    visited = set()
    queue = [start]
    visited.add(start)

    while queue:
        v = queue.pop(0)
        print(v, end=" ")

        for x in graph[v]:
            if x not in visited:
                visited.add(x)
                queue.append(x)

def dfs(v, visited):
    print(v, end=" ")
    visited.add(v)

    for x in graph[v]:
        if x not in visited:
            dfs(x, visited)

print("BFS Traversal:")
bfs(0)

print("\nDFS Traversal:")
dfs(0, set())
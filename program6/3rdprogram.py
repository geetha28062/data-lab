# Kruskal's Algorithm

n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

edges = []

for i in range(e):
    u, v, w = map(int, input(
        "Enter source, destination and weight: ").split())
    edges.append((w, u, v))

edges.sort()

parent = list(range(n))
cost = 0

def find(x):
    while parent[x] != x:
        x = parent[x]
    return x

print("Minimum Spanning Tree:")

count = 0

for w, u, v in edges:
    a = find(u)
    b = find(v)

    if a != b:
        print(u, "--", v, "=", w)
        parent[a] = b
        cost += w
        count += 1

        if count == n - 1:
            break

print("Minimum Cost:", cost)
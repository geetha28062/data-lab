# Kruskal's Algorithm with Union-Find

n = 5

edges = [
    (0, 1, 2),
    (0, 3, 6),
    (1, 2, 3),
    (1, 3, 8),
    (1, 4, 5),
    (2, 4, 7),
    (3, 4, 9)
]

parent = list(range(n))

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

edges.sort(key=lambda x: x[2])

cost = 0

print("Minimum Spanning Tree:")

for u, v, w in edges:
    a = find(u)
    b = find(v)

    if a != b:
        parent[a] = b
        print(u, "--", v, "=", w)
        cost += w

print("Minimum Cost:", cost)
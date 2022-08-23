import sys
sys.stdin = open("input.txt")


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


v, e = map(int, input().split())
parent = [0] * (v+1)

for i in range(1, v+1):
    parent[i] = i

edges = []
result = 0

for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

 # [(1, 3, 2), (1, 6, 4), (2, 1, 3), (2, 1, 6), (2, 2, 5), (3, 1, 2), (3, 4, 5), (3, 6, 5), (4, 3, 4), (4, 6, 7), (5, 5, 1), (6, 7, 3)]
edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        last = cost

print(result-last)

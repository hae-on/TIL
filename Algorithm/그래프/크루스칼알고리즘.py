import sys
sys.stdin = open("input.txt")


def find_parent(parent, x):
    # 루트 노드 아니면 찾을 때까지 재귀 호출
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
parent = [0] * (v + 1)

# 자기 자신으로 초기화
for i in range(1, v+1):
    parent[i] = i

edges = []
result = 0

for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

# 간선 비용순으로 정렬
# [(7, 3, 4), (13, 4, 7), (23, 4, 6), (25, 6, 7), (29, 1, 2), (34, 2, 6), (35, 2, 3), (53, 5, 6), (75, 1, 5)]
edges.sort()

for edge in edges:
    cost, a, b = edge
    # 싸이클 발생 안하는 경우만 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)

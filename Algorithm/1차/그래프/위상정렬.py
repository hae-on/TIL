from collections import deque
import sys
sys.stdin = open("input.txt")

v, e = map(int, input().split())
indegree = [0] * (v+1)
graph = [[] for _ in range(v+1)]

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1
    # [0, 0, 1, 1, 2, 1, 2, 1]


def topology_sort():
    result = []
    q = deque()

    # 처음 진입 시 진입차수 0인 노드 큐 삽입
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    for i in result:
        print(i, end=" ")


topology_sort()

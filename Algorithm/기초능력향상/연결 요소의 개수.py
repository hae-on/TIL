from pprint import pprint
import sys
sys.stdin = open("input.txt")

n, m = map(int, input().split())
graph = [[0] * (n+1) for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1][v2] = 1
    graph[v2][v1] = 1


def dfs(k):
    visited[k] = 1
    for i in range(n+1):
        if graph[i][k] == 1 and visited[i] == 0:
            dfs(i)


cnt = 0

for i in range(1, n+1):
    if not visited[i]:
        dfs(i)
        cnt += 1

pprint(cnt)

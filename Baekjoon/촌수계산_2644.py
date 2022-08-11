import sys
sys.stdin = open("input.txt")
from pprint import pprint

n = int(input())
a, b = map(int, input().split())
m = int(input())

graph = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    p, d = map(int, input().split())

    graph[p][d] = 1
    graph[d][p] = 1

# pprint(graph)

# 해당 번호의 전체 촌수
visited = [0] * (n+1)

def dfs(k):
    for i in range(n+1):
        if graph[i][k] ==1 and visited[i] == 0:
            visited[i] = visited[k] + 1
            dfs(i)
dfs(a)

# print(visited)
pprint(visited[b] if visited[b] > 0 else -1)
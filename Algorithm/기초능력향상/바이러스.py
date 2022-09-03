from pprint import pprint
import sys
sys.stdin = open("input.txt")

n = int(input())
m = int(input())

graph = [[0] * (n+1) for _ in range(n+1)]

for i in range(m):
    v1, v2 = map(int, input().split())
    graph[v1][v2] = 1
    graph[v2][v1] = 1

visited = [0] * (n+1)


def dfs(k):
    visited[k] = 1
    for i in range(n+1):
        if i == k:
            continue
        if graph[i][k] == 1 and visited[i] == 0:
            dfs(i)


dfs(1)

pprint(sum(visited)-1)

from pprint import pprint
import sys
sys.stdin = open("input.txt")

n = int(input())
a, b = map(int, input().split())
m = int(input())

graph = [[0] * (n + 1) for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1

visited = [0] * (n+1)


def dfs(k):
    for i in range(n+1):
        if graph[i][k] == 1 and visited[i] == 0:
            visited[i] = visited[k] + 1
            dfs(i)


dfs(a)

print(visited[b] if visited[b] > 0 else -1)

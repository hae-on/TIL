import sys
sys.stdin = open("input.txt")
from pprint import pprint

N = int(input())
M = int(input())

graph = [[0] * (N+1) for _ in range(N+1)]

for i in range(M):
    v1, v2 = map(int, input().split())
    graph[v1][v2] = 1
    graph[v2][v1] = 1

# pprint(graph)

visited = [0] * (N+1)

def dfs(k):
    visited[k] = 1
    for i in range(N+1):
        if i == k:
            continue
        # 해당 컴퓨터가 바이러스에 걸렸고 체크가 안 되었을 경우
        if graph[i][k] == 1 and visited[i] == 0:
            dfs(i)
dfs(1)

# 1번을 통해 걸린 컴퓨터이므로 1번은 빼줌
print(sum(visited)-1)






import sys
sys.stdin = open("input.txt")
from pprint import pprint

N, M = map(int, input().split())

graph = [[0] * (N+1) for _ in range(N+1)]

adj = [[] for _ in range(N+1)]

for i in range(M):
    v1, v2 = map(int, input().split())
    graph[v1][v2] = 1

    adj[v1].append(v2)

pprint(graph)      
pprint(adj)


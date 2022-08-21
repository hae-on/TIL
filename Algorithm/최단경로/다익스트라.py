from pprint import pprint
import sys
from tkinter.tix import Tree
sys.stdin = open("input.txt")

INF = int(1e9)
n, m = map(int, input().split())
start = int(input())
# [[], [], [], [], [], [], []]
graph = [[] for _ in range(n+1)]
# [False, False, False, False, False, False, False]
visited = [False] * (n+1)
# 최단 거리 테이블을 모두 무한으로 초기화
''' [1000000000,
 1000000000,
 1000000000,
 1000000000,
 1000000000,
 1000000000,
 1000000000]'''
distance = [INF] * (n+1)


# 간선 정보 입력
for _ in range(m):
    a, b, c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c
    graph[a].append((b, c))
    '''
    [[],
    [(2, 2), (3, 5), (4, 1)],
    [(3, 3), (4, 2)],
    [(2, 3), (6, 5)],
    [(3, 3), (5, 1)],
    [(3, 1), (6, 2)],
    []]
    '''


# 방문하지 않는 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index


def dijkstra(start):
    # 시작 노드 초기화
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        # [(2, 2), (3, 5), (4, 1)]
        # [1000000000, 0, 2, 5, 1, 1000000000, 1000000000]
        distance[j[0]] = j[1]
    # 시작 노드를 제외한 전체 n-1개의 노드에 대해 반복
    for i in range(n-1):
        # 현재 최단 거리가 가장 짧은 노드 꺼내서 방문 처리
        now = get_smallest_node()
        visited[now] = True
        # 현재 노드와 연결된 다른 노드 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost


dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print('INFINITY')
    else:
        print(distance[i])

import heapq
import sys
# input = sys.stdin.readline
sys.stdin = open("input.txt")
sys.setrecursionlimit(10**6)

n, e = map(int, input().split())
INF = int(1e9)
graph = [[] * (n+1) for _ in range(n+1)]


for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

x, y = map(int, input().split())


def dijkstra(start):
    distance = [INF] * (n+1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    return distance


original_dis = dijkstra(1)
x_dis = dijkstra(x)
y_dis = dijkstra(y)

# 1 => v1 => v2 => N
# 1 => v2 => v1 => N

x_path = original_dis[x] + x_dis[y] + y_dis[n]
y_path = original_dis[y] + y_dis[x] + x_dis[n]

result = min(x_path, y_path)
print(result if result < INF else -1)

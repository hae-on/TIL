from collections import deque
import sys
sys.stdin = open("input.txt")

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

cnt = 0
answer = 0

def bfs(i, j):
    graph[i][j] = 0
    q = deque()
    q.append([i, j])
    w = 1
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0<= nx < n and 0<= ny <m and graph[nx][ny] ==1:
                q.append([nx, ny])
                graph[nx][ny] = 0
                w += 1
    return w
            
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            cnt += 1
            answer = max(bfs(i, j), answer)

print(cnt)
print(answer)


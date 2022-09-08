from collections import deque
import sys
sys.stdin = open("input.txt")

n = int(input())
board = [list(map(int, input())) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

house = []
cnt = 0


def bfs(i, j):
    board[i][j] = 0
    q = deque()
    q.append([i, j])
    w = 1
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 1:
                q.append([nx, ny])
                board[nx][ny] = 0
                w += 1
    return w


for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            cnt += 1
            house.append(bfs(i, j))

house.sort()

print(cnt)
print(*house, sep="\n")

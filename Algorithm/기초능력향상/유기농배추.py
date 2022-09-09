from collections import deque
from pprint import pprint
import sys
sys.stdin = open("input.txt")

t = int(input())

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(i, j):
    board[i][j] = 0
    q = deque()
    q.append([i, j])

    while q:
        x, y = q.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if board[nx][ny] == 1:
                board[nx][ny] = 0
                q.append([nx, ny])


for _ in range(t):
    m, n, k = map(int, input().split())
    board = [[0] * n for _ in range(m)]

    for _ in range(k):
        v1, v2 = map(int, input().split())
        board[v1][v2] = 1

    cnt = 0

    for i in range(m):
        for j in range(n):
            if board[i][j] == 1:
                bfs(i, j)
                cnt += 1

    print(cnt)

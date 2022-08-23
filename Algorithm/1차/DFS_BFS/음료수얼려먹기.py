import sys
sys.stdin = open("input.txt")

N, M = map(int, input().split())
board = [list(map(int, input())) for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y):
    board[x][y] = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<= nx < N and 0<= ny < M:
            if board[nx][ny] == 0:
                dfs(nx, ny)

cnt = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            dfs(i, j)
            cnt += 1

print(cnt)
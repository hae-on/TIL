import sys
sys.stdin = open("input.txt")

sys.setrecursionlimit(10000)


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

answer = 0


def dfs(i, j, k):
    for d in range(4):
        nx = i + dx[d]
        ny = j + dy[d]

        if 0 <= nx < n and 0 <= ny < n and board[nx][ny] > k and shrink[nx][ny] == 0:
            shrink[nx][ny] = 1
            dfs(nx, ny, k)


for k in range(max(map(max, board))):
    cnt = 0
    shrink = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if board[i][j] > k and shrink[i][j] == 0:
                shrink[i][j] = 1
                cnt += 1
                dfs(i, j, k)

    answer = max(answer, cnt)

print(answer)

import sys
sys.stdin = open("게임개발.txt")

n, m = map(int, input().split())
x, y, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

board[x][y] = 1


def turn_left():
    global d
    d -= 1
    if d < 0:
        d = 3


cnt = 1
check = 0

while True:
    turn_left()

    nx = x + dx[d]
    ny = y + dy[d]

    if board[nx][ny] == 0 and visited[nx][ny] == 0:
        visited[nx][ny] = 1
        cnt += 1
        check = 0
        x = nx
        y = ny
    else:
        check += 1

    if check == 4:
        nx = x - dx[d]
        ny = y - dy[d]

        if board[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        check = 0

print(cnt)

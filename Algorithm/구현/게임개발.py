import sys
sys.stdin = open("input.txt")

N, M = map(int, input().split())
x, y, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

board[x][y] = 1

# 북 동 남 서
dx = [-1,0,1,0]
dy = [0,1,0,-1]


def turnLeft():
    global d
    d -= 1
    if d == -1:
        d = 3

cnt = 1
check = 0

while True:
    turnLeft()

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


    
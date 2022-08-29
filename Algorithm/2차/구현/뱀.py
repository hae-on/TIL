import sys
sys.stdin = open("뱀.txt")

n = int(input())
k = int(input())
board = [[0] * (n+1) for _ in range(n+1)]

for _ in range(k):
    a, b = map(int, input().split())
    board[a][b] = 1

l = int(input())
info = []
for _ in range(l):
    x, c = input().split()
    info.append((int(x), c))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def turn(dir_, c):
    if c == 'L':
        dir_ = (dir_-1) % 4
    else:
        dir_ = (dir_+1) % 4
    return dir_


def simulate():
    x = 1
    y = 1
    board[x][y] = 2
    dir_ = 0
    time = 0
    index = 0
    q = [(x, y)]

    while True:
        nx = x + dx[dir_]
        ny = y + dy[dir_]

        if 1 <= nx <= n and 1 <= ny <= n and board[nx][ny] != 2:
            if board[nx][ny] == 0:
                board[nx][ny] = 2
                q.append((nx, ny))
                px, py = q.pop(0)
                board[px][py] = 0
            if board[nx][ny] == 1:
                board[nx][ny] = 2
                q.append((nx, ny))
        else:
            time += 1
            break
        x, y = nx, ny
        time += 1
        if index < 1 and time == info[index][0]:
            dir_ = turn(dir_, info[index][1])
            index += 1
    return time


print(simulate())

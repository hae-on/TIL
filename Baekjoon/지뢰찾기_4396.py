import sys
sys.stdin = open("input.txt")

n = int(input())

game_board = []
open_board = []

for _ in range(n):
    game_board.append(list(input()))

for _ in range(n):
    open_board.append(list(input()))

result_board = [['.']*n for _ in range(n)]


dx = [-1, 0, 1, -1, 1, -1, 0, 1]
dy = [-1, -1, -1, 0, 0, 1, 1, 1]

flag = False

for i in range(n):
    for j in range(n):
        if open_board[i][j] == 'x':
            cnt = 0
            for k in range(8):
                x = i + dx[k]
                y = j + dy[k]
            
                if 0<=x<=n-1 and 0<=y<=n-1:
                    if game_board[x][y] == '*':
                        cnt += 1
            
            result_board[i][j] = str(cnt)

            if game_board[i][j] == '*':
                flag = True

if flag:
    for x in range(n):
        for y in range(n):
            if game_board[x][y] == '*':
                result_board[x][y] = '*'

for i in result_board:
    print(''.join(i))
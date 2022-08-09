# 우 하 우하 우상 (제일 왼쪽 돌을 골라야하므로)
dx = [0, 1, -1, 1]
dy = [1, 0, 1, 1]

black = 1
white = 2
N = 19
board = [list(map(int, input().split())) for _ in range(N)]
flag = 0

for x in range(N):
    for y in range(N):
        if board[x][y] == black or board[x][y] == white:
            for d in range(4):
                stone = 1
                nx = x + dx[d]
                ny = y + dy[d]

                while True:
                    if not(0<= nx < N and 0 <= ny < N):
                        break
                    # 다른색 돌이면 탈출
                    if board[x][y] != board[nx][ny]:
                        break

                    stone += 1

                    nx = nx + dx[d]
                    ny = ny + dy[d]
                
                if stone == 5:
                    #이전 좌표
                    prev_x = x - dx[d]
                    prev_y = y - dy[d]

                    #육목 체크
                    if not(0 <= prev_x < N and 0 <= prev_y < N) or board[x][y] != board[prev_x][prev_y]:
                        print(board[x][y])
                        print(x+1, y+1)
                        flag = board[x][y]
if not flag:
    print(flag)

# board = [list(map(int, input().split())) for _ in range(19)]

# # 옆, 아래, 대각선 아래, 대각선 위
# dx = [0, 1, 1, -1]
# dy = [1, 0, 1, 1]

# for x in range(19):
#     for y in range(19):
#         if board[x][y] != 0:
#             target = board[x][y]
        
#             for i in range(4):
#                 nx = x + dx[i]
#                 ny = y + dy[i]
#                 stone = 1

#                 while 0 <= nx <19 and 0 <= ny < 19 and board[nx][ny] == target:
#                     stone += 1
#                     if stone == 5:
#                         # 5개일 때 육목 체크
#                         if 0 <= x - dx[i] < 19 and 0 <= y - dy[i] < 19 and board[x - dx[i]][y - dy[i]] == target:
#                             break
#                         if 0 <= nx + dx[i] <19 and 0 <= ny + dy[i] <19 and board[nx + dx[i]][ny + dy[i]] == target:
#                             break
                        
#                         print(target)
#                         print(x + 1, y + 1)
#                         exit(0)
                    
#                     nx += dx[i]
#                     ny += dy[i]
# print(0)


board = [list(map(int, input().split())) for _ in range(19)]

# 옆, 아래, 대각선 아래, 대각선 위
dx = [0, 1, 1, -1]
dy = [1, 0, 1, 1]

for x in range(19):
    for y in range(19):
        if board[x][y] != 0:
            target = board[x][y]
        
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                stone = 1

                while 0 <= nx <19 and 0 <= ny < 19 and board[nx][ny] == target:
                    stone += 1
                    if stone == 5:
                        # 5개일 때 육목 체크
                        if 0 <= x - dx[i] < 19 and 0 <= y - dy[i] < 19 and board[x - dx[i]][y - dy[i]] == target:
                            break
                        if 0 <= nx + dx[i] <19 and 0 <= ny + dy[i] <19 and board[nx + dx[i]][ny + dy[i]] == target:
                            break
                        
                        print(target)
                        print(x + 1, y + 1)
                        exit(0)
                    
                    nx += dx[i]
                    ny += dy[i]
print(0)
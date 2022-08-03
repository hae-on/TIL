board = []
cnt = 0

for _ in range(8):
    board.append(input())

for i in range(8):
    for j in range(8):
        if i % 2 == 0 and j % 2 == 0 and board[i][j] == 'F':
            cnt += 1
        if i % 2 == 1 and j % 2 == 1 and board[i][j] == 'F':
            cnt += 1
    
print(cnt)

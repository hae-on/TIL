N, M = map(int, input().split())

row = N
col = M

castle =[]

for _ in range(N):
    castle.append(input())

for i in range(N):
    for j in range(M):
        if castle[i][j] == 'X':
            row -= 1
            break

for i in range(M):
    for j in range(N):
        if castle[j][i] == 'X':
            col -= 1
            break

print(max(row, col))
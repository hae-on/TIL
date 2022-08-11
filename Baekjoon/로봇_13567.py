import sys
sys.stdin = open("input.txt")

M, N = map(int,input().split())

# 오른 위 왼 아래
dx = [0,1,0,-1]
dy = [1,0,-1,0]

d = 0
x = 0
y = 0

flag = True

for _ in range(N):
    a, b = input().split()
    dir_x = dx[d%4]
    dir_y = dy[d%4]

    if a == 'MOVE':
        nx = x + dir_x * int(b)
        ny = y + dir_y * int(b)

        # print(nx, ny)

        #move 하다가 밖으로 나가버리는 경우 체크
        if 0<= nx < M and 0<= ny < M:
            x = nx
            y = ny
        else:
            flag = False
    else:
        if b == '0':
            d += 1
        elif b == '1':
            d -= 1

if not flag:
    print(-1)
else:
    print(y, x) 




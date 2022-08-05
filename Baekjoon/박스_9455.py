import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    m, n = map(int, input().split())
    box = [list(map(int, input().split())) for _ in range(m)]
    
    col_list = []
    for x in range(n):
        col = []
        for y in range(m):
            col.append(box[y][x])
        col.reverse()
        col_list.append(col)

    
    cnt = 0
    for i in range(n):
        floor = 0
        for j in range(m):
            if col_list[i][j] == 1:
                cnt += floor - j
                floor += 1
    
    print(abs(cnt))
# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    result = []
    for i in range(n):
        tmp = []
        for j in range(i+1):
            if j == 0 or j == i:
                tmp.append(1)
            else:
                tmp.append(result[i-1][j] + result[i-1][j-1])
        result.append(tmp)

    print(f'#{tc}')
    for i in result:
        print(*i)

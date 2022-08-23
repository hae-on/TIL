import sys
sys.stdin = open("input.txt")

N, K = map(int, input().split())

cnt = 0

while N >= K:
    if N % K != 0:
        N -= 1
        N //= K
        cnt += 1
    else:
        N //= K
        cnt += 1

print(cnt)
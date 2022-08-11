import sys
sys.stdin = open("input.txt")

N = int(input())
bridge = [-1] * (N+1)
cnt = 0

for _ in range(N):
    cow, position = map(int, input().split())
    
    if bridge[cow] == -1:
        bridge[cow] = position
    else:
        if bridge[cow] != position:
            cnt += 1
            bridge[cow] = position

    print(bridge)
    print(cnt)
# print(cnt)
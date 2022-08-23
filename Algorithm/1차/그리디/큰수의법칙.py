import sys
sys.stdin = open("input.txt")

N, M, K = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

max_ = arr[N-1]
second_max = arr[N-2]

answer = 0

while True:
    for i in range(K):
        if M == 0:
            break
        answer += max_ 
        M -= 1
    if M == 0:
        break
    answer += second_max
    M -= 1


print(answer)





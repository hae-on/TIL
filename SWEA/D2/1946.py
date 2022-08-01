import sys
sys.stdin = open("input.txt", "r")

T= int(input())

for tc in range(1, T+1):
    N = int(input())
    answer =''
    for i in range(N):
        word, num = input().split()
        answer += word * int(num)

    print(f'#{tc}')

    for i in range(0, len(answer), 10):
        print(answer[i:i+10])
import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    prime_list =[2, 3, 5, 7, 11]
    cnt_list = [0] * 5
    
    for i in range(len(prime_list)):
        while True:
            if N % prime_list[i] == 0:
                N = N // prime_list[i]
                cnt_list[i] += 1
            else:
                break

    print(f'#{tc} ', end="")
    print(*cnt_list)
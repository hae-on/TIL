# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    # 0에서 9까지 셀 수 있는 배열 생성
    numbers = [0] * 10
    # 배수 변수 (1에서부터 k까지 증가)
    i = 1
    # 배열에 하나라도 0이 있는 동안 진행
    while 0 in numbers:
        # 증가해나가는 수
        num = str(N * i)
        for j in range(len(num)):
            numbers[int(num[j])] += 1
        i += 1
    print(f'#{tc} {num}')

import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    distance = 0
    speed = 0

    for i in range(N):
        car = list(map(int, input().split()))
        # 유지
        if car[0] == 0:
            # 스피드는 그대로 거리만 이동
            distance += speed
        # 가속
        elif car[0] == 1:
            speed += car[1]
            distance += speed
        # 감속
        else:
            # 현재 속도가 더 작을 경우 음수 방지
            if car[1] > speed:
                speed = 0
            else:
                speed -= car[1]
                distance += speed

    print(f'#{tc} {distance}')

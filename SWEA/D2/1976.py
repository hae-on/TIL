import sys
sys.stdin = open("input.txt", "r")

T = int(input())


def time_sum(time1, time2):
    H1, M1 = time1[0], time1[1]
    H2, M2 = time2[0], time2[1]

    plus_hours = 0

    minite_sum = M1 + M2

    # 60분이 넘으면 한 시간으로 넘겨주기
    if minite_sum >= 60:
        minite_sum -= 60
        plus_hours += 1

    hours_sum = H1 + H2 + plus_hours

    # 13시는 없으므로 12시가 넘으면 다시 1시부터 시작
    if hours_sum > 12:
        hours_sum -= 12

    return f'{hours_sum} {minite_sum}'


for tc in range(1, T+1):
    time = list(map(int, input().split()))
    # 앞 시간과 뒷 시간으로 쪼개기
    time1, time2 = time[:2], time[2:]

    print(f'#{tc} {time_sum(time1, time2)}')

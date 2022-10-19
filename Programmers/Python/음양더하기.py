def solution(absolutes, signs):
    sum_n = 0
    for i in range(len(absolutes)):
        if signs[i] == 'true':
            sum_n += absolutes[i]
        else:
            sum_n -= absolutes[i]
    return sum_n


print(solution([4, 7, 12], ['true', 'false', 'true']))

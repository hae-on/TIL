n = int(input())


def solution(n):
    answer = 0

    while n > 0:
        answer += n % 10
        n = n // 10
    return answer


print(solution(n))

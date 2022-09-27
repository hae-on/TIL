import sys

sys.stdin = open("input.txt")
from itertools import combinations

t = int(input())


def combi(food):
    result = 0
    for a, b in list(combinations(food, 2)):
        result += foods[a][b] + foods[b][a]
    return result


def dfs(idx, d):
    global min_
    if idx == n // 2:
        A = []
        B = []
        for i in range(n):
            if visited[i]:
                A.append(i)
            else:
                B.append(i)
        result = abs(combi(A) - combi(B))
        min_ = min(min_, result)
        return

    for i in range(d, n):
        if visited[i] == 0:
            visited[i] = 1
            dfs(idx + 1, i + 1)
            visited[i] = 0


for tc in range(1, t + 1):
    n = int(input())
    foods = [list(map(int, input().split())) for _ in range(n)]
    min_ = 1e9
    visited = [0] * n
    dfs(0, 0)
    print(f"#{tc} {min_}")

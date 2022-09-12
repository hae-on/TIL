import sys
sys.stdin = open("input.txt")

n = int(input())
arr = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

max_ = -1e9
min_ = 1e9


def dfs(x, data):
    global add, sub, mul, div, max_, min_

    if x == n:
        max_ = max(max_, data)
        min_ = min(min_, data)
    else:
        if add > 0:
            add -= 1
            dfs(x+1, data + arr[x])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(x+1, data - arr[x])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(x+1, data * arr[x])
            mul += 1
        if div > 0:
            div -= 1
            dfs(x+1, int(data / arr[x]))
            div += 1


dfs(1, arr[0])

print(max_)
print(min_)

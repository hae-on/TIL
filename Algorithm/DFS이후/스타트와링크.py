import sys
sys.stdin = open("input.txt")

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [False for _ in range(n+1)]
min_ = 1e9


def dfs(depth, idx):
    global min_
    if depth == n // 2:
        start = 0
        link = 0
        for i in range(n):
            for j in range(i+1, n):
                if i == j:
                    continue
                if visited[i] and visited[j]:
                    start += board[i][j] + board[j][i]
                elif not visited[i] and not visited[j]:
                    link += board[i][j] + board[j][i]
        min_ = min(min_, abs(start-link))

    for i in range(idx, n):
        if not visited[i]:
            visited[i] = True
            dfs(depth+1, i+1)
            visited[i] = False


dfs(0, 0)
print(min_)

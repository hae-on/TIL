import sys
sys.stdin = open("input.txt")

#Python이 정한 최대 재귀 깊이보다 재귀의 깊이가 더 깊어질 때 생기는 오류 방지
# import sys
# sys.setrecursionlimit(10**6)

dx=[-1, -1, 0, 1, 1, 1, 0, -1];
dy=[0, 1, 1, 1, 0, -1, -1, -1];

def dfs(i, j):
    board[i][j] = 0
    for d in range(8):
        nx = i + dx[d]
        ny = j + dy[d]

        if 0 <= nx < h and 0 <= ny < w and board[nx][ny] ==1:
            dfs(nx, ny)


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    
    board = []
    for _ in range(h):
        board.append(list(map(int, input().split())))
    
    answer = 0
    for i in range(h):
        for j in range(w):
            if board[i][j] == 1:
                board[i][j] = 0
                answer += 1
                dfs(i, j)

    print(answer)


from collections import deque
import sys
sys.stdin = open("input.txt")

N, M = map(int, input().split())
board = [list(map(int,input())) for _ in range(N)]

dx = [-1, 1, 0, 0] 
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 1:
                queue.append((nx, ny))
                board[nx][ny] = board[x][y]+1
    
    return board[N-1][M-1]

print(bfs(0,0))
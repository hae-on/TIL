from collections import deque
import sys
sys.stdin = open("input.txt")

n, k = map(int, input().split())
max_ = 10 ** 5
visited = [0] * (max_ + 1)


def bfs():
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        if x == k:
            print(visited[x])
            break
        for nx in (x-1, x+1, x*2):
            if 0 <= nx <= max_ and not visited[nx]:
                visited[nx] = visited[x] + 1
                q.append(nx)


bfs()

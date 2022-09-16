from collections import deque
import sys
sys.stdin = open("input.txt")

n, k = map(int, input().split())
max_ = 10 ** 5
visited = [0] * (max_ + 1)
cnt = 0


def bfs():
    global cnt
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        if x == k:
            cnt += 1
            continue
        for nx in (x-1, x+1, x*2):
            if 0 <= nx < max_:
                if not visited[nx] or visited[nx] == visited[x]+1:
                    visited[nx] = visited[x] + 1
                    q.append(nx)


bfs()

print(visited[k])
print(cnt)

from collections import deque
import copy
import sys
sys.stdin = open("input.txt")

v = int(input())
indegree = [0] * (v+1)
graph = [[] for _ in range(v+1)]
time = [0] * (v+1)

for i in range(1, v+1):
    data = list(map(int, input().split()))
    # [0, 10, 10, 4, 4, 3]
    time[i] = data[0]
    for x in data[1:-1]:
        indegree[i] += 1
        # [[], [2, 3, 4], [], [4, 5], [], []]
        graph[x].append(i)


def topology_sort():
    result = copy.deepcopy(time)
    q = deque()

    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        for i in graph[now]:
            result[i] = max(result[i], result[now] + time[i])
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    for i in range(1, v+1):
        print(result[i])


topology_sort()

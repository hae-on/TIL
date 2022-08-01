# import sys
# input = sys.stdin.readline

N, M = map(int, input().split())
arr = []

answer = 'Yes'

for i in range(M):
    dummy = int(input())
    book = list(map(int, input().split()))

    for j in range(dummy -1):
        print(j)
        # j > j+1 이어야 원하는대로 뺄 수 있음
        if book[j] < book[j+1]:
            answer = 'No'
            break
    
print(answer)
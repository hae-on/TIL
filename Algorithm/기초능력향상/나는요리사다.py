import sys
sys.stdin = open("input.txt")

n = 5

list_ = [list(map(int,input().split())) for _ in range(n)]
score = []

for i in range(n):
    sum_ = 0
    for j in range(n-1):
        sum_ += list_[i][j]
    score.append(sum_)

print(score.index(max(score))+1,max(score))
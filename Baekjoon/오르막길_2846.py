N = int(input())
Pi = list(map(int, input().split()))

uphill = []
tmp = 0

for i in range(len(Pi)-1):
    tmp = Pi[i+1] - Pi[i]
    if tmp > 0:
        uphill.append(tmp)
    else:
        uphill.append(0)

# uphill = [1, 0, 3, 2]

answer = []
sum_ = 0

for i in uphill:
    if i > 0:
        sum_ += i
    else:
        answer.append(sum_)
        sum_ = 0
answer.append(sum_)

#answer = [1, 5]
print(max(answer))

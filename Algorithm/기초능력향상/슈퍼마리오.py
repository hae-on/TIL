import sys
sys.stdin = open("input.txt")

n = 10
mushroom = []

for _ in range(n):
    mushroom.append(int(input()))

sum_ = 0
tmp = 0
for i in mushroom:
    sum_ += i
    if sum_ == 100:
        break
    elif sum_ > 100:
        tmp = sum_ - i
        if 100-tmp >= sum_-100:
            print(sum_)
            break
        else:
            print(tmp)
            break
else:
    print(sum_)

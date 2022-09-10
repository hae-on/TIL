import sys
sys.stdin = open("input.txt")

x = input()
cnt = 0

def check(y, cnt):
    if len(y) > 1:
        cnt += 1
        sum_ = 0
        for i in y:
            sum_ += int(i)
        check(str(sum_), cnt)
    else:
        if int(y) % 3 == 0:
            print(cnt)
            print("YES")
        else:
            print(cnt)
            print("NO")

check(x, cnt)
import sys
sys.stdin = open("input.txt")

# import sys
# input = sys.stdin.readline

N = int(input())
cnt = 0
d={}


for i in range(1, N+1):
    name = input()
    #sys.stdin.readline 사용시 if name=="ENTER\n"
    if name=="ENTER":
        d={}
        continue
    else:
        if name not in d:
            d[name]=1
            cnt += 1


print(cnt)
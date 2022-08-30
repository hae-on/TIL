import sys
sys.stdin = open("input.txt")

n = int(input())
d = {}

for i in range(n):
    file_ = input()
    name = file_.split('.')[1]

    if name in d:
        d[name] += 1
    else:
        d[name] = 1

d = sorted(d.items())

for k, v in d:
    print(k.rstrip(), v)

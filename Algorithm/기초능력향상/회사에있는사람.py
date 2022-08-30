import sys
sys.stdin = open("input.txt")

n = int(input())
d = {}

for i in range(n):
    name, status = input().split()

    if status == 'enter':
        d[name] = 'enter'
    else:
        if d[name]:
            del d[name]

d = sorted(d.items(), reverse=True)

for i in d:
    print(i[0])

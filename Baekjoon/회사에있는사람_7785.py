import sys
sys.stdin = open("input.txt")

n = int(input())
d = {}


for _ in range(1, n+1):
    name, status = input().split()

    if status == 'enter':
        d[name] = 'enter'
    else:
        if d[name]:
            del d[name]

sorted_dict = sorted(d.items(), reverse=True)

for i in sorted_dict:
    print(i[0])

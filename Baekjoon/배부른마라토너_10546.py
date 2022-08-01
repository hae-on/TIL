import sys
sys.stdin = open("input.txt")


N = int(sys.stdin.readline())
d = {}

for i in range(2*N-1):
    name = sys.stdin.readline().strip()
    d[name] = d.get(name, 0) + 1

for key, value in d.items():
    if value % 2 != 0:
        print(key)
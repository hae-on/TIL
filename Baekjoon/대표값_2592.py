import sys
sys.stdin = open("input.txt")

num = []
for i in range(10):
    num.append(int(input()))

print(int(sum(num) / 10))
print(max(num, key = num.count))

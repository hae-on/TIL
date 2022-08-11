import sys
sys.stdin = open("input.txt")

W = []
for _ in range(10):
    N = int(input())
    W.append(N)

sorted_W = sorted(W, reverse=True)

K = []
for _ in range(10):
    N = int(input())
    K.append(N)

sorted_K = sorted(K, reverse=True)


print(sum(sorted_W[:3]), sum(sorted_K[:3]))
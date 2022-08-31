import sys
sys.stdin = open("input.txt")

A = list(map(int, input().split()))
B = list(map(int, input().split()))

a_score = 0
b_score = 0
for i in range(len(A)):
    if A[i] > B[i]:
        a_score += 3
    elif A[i] < B[i]:
        b_score += 3
    else:
        a_score += 1
        b_score += 1

print(a_score, b_score)

if a_score > b_score:
    print('A')
elif a_score < b_score:
    print('B')
else:
    print('D')

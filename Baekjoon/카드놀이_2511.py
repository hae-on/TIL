import sys
sys.stdin = open("input.txt")

A = list(map(int, input().split()))
B = list(map(int, input().split()))

scoreA = 0
scoreB = 0

result = 'D'

for i in range(10):
    if A[i] > B[i]:
        scoreA += 3
        result = 'A'
    elif B[i] > A[i]:
        scoreB += 3
        result = 'B'
    elif A[i] == B[i]:
        scoreA += 1
        scoreB += 1

if scoreA > scoreB:
    print(scoreA, scoreB)
    print('A')
elif scoreB > scoreA:
    print(scoreA, scoreB)
    print('B')
elif scoreA == scoreB:
    if result == 'A':
        print(scoreA, scoreB)
        print('A')
    elif result == 'B':
        print(scoreA, scoreB)
        print('B')
    elif result == 'D':
        print(scoreA, scoreB)
        print('D')

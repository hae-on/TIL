A, B = map(str, input().split())
SA = A[::-1]
SB = B[::-1]

if SA > SB:
    print(SA)
else:
    print(SB)

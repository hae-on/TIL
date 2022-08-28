import sys
sys.stdin = open("럭키스트레이트.txt")

N = input()
length = int(len(N))
half_length = int(len(N) / 2)
left_n = N[:half_length]
right_n = N[half_length:length]

left = 0
for i in left_n:
    left += int(i)

right = 0
for i in right_n:
    right += int(i)

if left == right:
    print('LUCKY')
else:
    print('READY')

N = int(input())

for tc in range(1, N+1):
    r, e, c = list(map(int, input().split()))

    if e - c > r :
        print('advertise')
    elif e - c == r :
        print('does not matter')
    else:
        print('do not advertise')
  
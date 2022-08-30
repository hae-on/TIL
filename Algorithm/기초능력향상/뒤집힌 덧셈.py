x, y = input().split()

rev_x = int(x[::-1])
rev_y = int(y[::-1])
print(str(rev_x + rev_y)[::-1])

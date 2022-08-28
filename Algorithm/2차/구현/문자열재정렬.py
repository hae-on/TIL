import sys
sys.stdin = open("문자열재정렬.txt")

s = input()
str_ = []
num_ = []

for i in s:
    if i.isdigit() == False:
        str_.append(i)
    else:
        num_.append(int(i))

str_.sort()
str_.append(str(sum(num_)))

print(''.join(str_))

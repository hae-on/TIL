s = input()
s = s.upper()
alp = [0] * 26

for i in s:
    ascii_ = ord(i)-65
    alp[ascii_] += 1

max_ = max(alp)

if alp.count(max_) > 1:
    print('?')
else:
    print(chr((alp.index(max_))+65))

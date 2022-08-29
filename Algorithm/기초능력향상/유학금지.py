s = input()
list_ = ['C', 'A', 'M', 'B', 'R', 'I', 'D', 'G', 'E']

for i in list_:
    s = s.replace(i, '').strip()

print(s)

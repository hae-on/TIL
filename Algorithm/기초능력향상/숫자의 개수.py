a = int(input())
b = int(input())
c = int(input())

list_ = [0] * 10
abc = str(a * b * c)

for i in abc:
    list_[int(i)] += 1

print(*list_, sep='\n')

n = int(input())

d = {}
for i in range(n):
    s = input()

    if s in d:
        d[s] += 1
    else:
        d[s] = 1

best = max(d.values())
book = []

for i in d:
    if d[i] == best:
        book.append(i)

book.sort()
print(book[0])

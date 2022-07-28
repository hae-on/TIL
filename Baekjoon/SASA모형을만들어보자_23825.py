rest = []
for i in range(10):
    value = int(input())
    rest.append(value % 42)

print(len(set(rest)))

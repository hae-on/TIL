num = set(range(1, 10001))
generators = set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    generators.add(i)

self_nums = sorted(num - generators)

for self_num in self_nums:
    print(self_num)
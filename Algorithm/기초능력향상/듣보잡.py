nh, ns = map(int, input().split())

no_hear = set()
for _ in range(nh):
    no_hear.add(input())

no_see = set()
for _ in range(ns):
    no_see.add(input())

no_see_hear = sorted(list(no_hear & no_see))

print(len(no_see_hear))
for i in no_see_hear:
    print(i)

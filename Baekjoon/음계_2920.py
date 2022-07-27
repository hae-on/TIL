n = list(map(int, input().split()))

asc = 0
desc = 0

for i in range(len(n)-1):
    if n[i] - n[i+1] == -1:
        asc += 1
    elif n[i] - n[i+1] == 1:
        desc += 1

if asc == 7:
    print("ascending")
elif desc == 7:
    print("descending")
else:
    print("mixed")

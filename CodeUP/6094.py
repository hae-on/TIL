n = int(input())
a = list(map(int, input().split()))

x = a[0]

for i in range(n):
    if(x > a[i]):
        x = a[i]

print(x)

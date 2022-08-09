import sys
sys.stdin = open("input.txt")

list_ = []
for _ in range(5):
    list_.append(int(input()))

list_.sort()

print(int(sum(list_) / len(list_)))
print(list_[2])
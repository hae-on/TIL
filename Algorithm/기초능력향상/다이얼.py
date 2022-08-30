s = input()
time = 0

for i in s:
    ascii_ = ord(i)

    if ascii_ <= 67:
        time += 3
    elif ascii_ <= 70:
        time += 4
    elif ascii_ <= 73:
        time += 5
    elif ascii_ <= 76:
        time += 6
    elif ascii_ <= 79:
        time += 7
    elif ascii_ <= 83:
        time += 8
    elif ascii_ <= 86:
        time += 9
    elif ascii_ <= 90:
        time += 10

print(time)

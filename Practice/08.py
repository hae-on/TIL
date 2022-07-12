numbers = [0, 20, 100]
largest = numbers[0]
largest2 = None

for i in numbers[1:]:
    if i > largest:
        largest2 = largest
        largest = i
    elif largest2 is None or largest2 < i:
        largest2 = i

print(largest2)

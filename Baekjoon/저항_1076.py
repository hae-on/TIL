import sys
sys.stdin = open("input.txt")

colors = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']

color1 = str(colors.index(input()))
color2 = str(colors.index(input()))
color3 = colors.index(input())

print(int(color1 + color2) * 10 ** color3)


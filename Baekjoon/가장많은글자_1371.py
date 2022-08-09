import sys
sys.stdin = open("input.txt")

import sys
sentence = sys.stdin.read().replace("\n","").replace(" ","")

alp = [0] * 26

for i in sentence:
    alp[ord(i)-97] += 1

max_ = max(alp)
for i in range(26):
    if alp[i] == max_:
        print(chr(i+97), end="")
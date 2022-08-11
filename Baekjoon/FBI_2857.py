import sys
sys.stdin = open("input.txt")

FBI = []

for i in range(5):
    name = input()
    fbi_cnt = name.count('FBI')
    if fbi_cnt > 0:
        # str 처리해야 type error 방지
        FBI.append(str(i+1))

# *FBI 사용시 H E G O T A W A Y!로 틀림 
print(' '.join(FBI) if FBI else 'HE GOT AWAY!')
# https://www.acmicpc.net/problem/17398
N,S = int(input()),input()

score =0
bonus =0

for idx,OX in enumerate(S):
    if OX == 'O':
        score = score +1 + idx + bonus
        bonus += 1
    else:
        bonus = 0

print(score)
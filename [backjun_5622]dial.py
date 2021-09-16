# https://www.acmicpc.net/problem/5622

string = list(input())

answer = 0

for i in string:
    if i == 'A' or i == 'B' or i == 'C':
        answer += 3
        continue
    elif i == 'D' or i == 'E' or i == 'F':
        answer += 4
        continue
    elif i == 'G' or i == 'H' or i == 'I':
        answer += 5
        continue
    elif i == 'J' or i == 'K' or i == 'L':
        answer += 6
        continue
    elif i == 'M' or i == 'N' or i == 'O':
        answer += 7
        continue
    elif i == 'P' or i == 'Q' or i == 'R' or i == 'S':
        answer += 8
        continue
    elif i == 'T' or i == 'U' or i == 'V':
        answer += 9
        continue
    else:
        answer += 10
        continue


print(answer)

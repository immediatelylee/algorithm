# https://www.acmicpc.net/problem/8958
n = int(input())

for _ in range(n):
    OX = input()
    bonus = False
    result = 0
    count = 0
    for i in OX:
        if i == 'O' and bonus == True:
            result += 1
            count += 1
            result += count
        elif i == 'O':
            result += 1
            bonus = True
        else:
            count = 0
            bonus = False
    print(result)

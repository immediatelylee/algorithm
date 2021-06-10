# https://www.acmicpc.net/problem/1874
# 스택 ,그리디 문제

n = int(input())

count = 1
stack = []
result = []

for i in range(n):
    data = int(input())
    while count <= data:
        stack.append(count)
        count += 1
        result.append('+')
    if stack[-1] == data:
        stack.pop()
        result.append('-')
    else:
        print('NO')
        exit(0)

print('\n'.join(result))

# while if else 의 flow join함수 사용

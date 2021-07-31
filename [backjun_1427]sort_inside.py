# https://www.acmicpc.net/problem/1427

N = list(input())
result = []
for i in range(len(N)):
    result.append(int(N[i]))

result.sort(reverse=True)

for i in range(len(result)):
    print(result[i], end='')

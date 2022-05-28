# https://www.acmicpc.net/problem/10814

result = []
for i in range(int(input())):
    age, name = input().split()
    result.append([int(age), name])

A = sorted(result, key=lambda x: x[0])

for i in range(len(A)):
    print(A[i][0], A[i][1])

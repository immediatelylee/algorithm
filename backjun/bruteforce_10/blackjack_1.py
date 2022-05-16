# https://www.acmicpc.net/problem/2798

n, m = map(int, input().split())
cardlist = list(map(int, input().split()))
result = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            tmp = cardlist[i]+cardlist[j]+cardlist[k]
            if tmp <= m and result <= tmp:
                result = tmp

print(result)

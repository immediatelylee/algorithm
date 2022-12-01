n, m = map(int, input().split())
money_type = []
for i in range(n):
    money_type.append(int(input()))

dp = [10001 for i in range(m+1)]
dp[0] = 0

for i in range(n):
    for j in range(money_type[i], m+1, money_type[i]):
        if dp[j-money_type[i]] != 10001:
            dp[j] = min(dp[j], dp[j-money_type[i]]+1)

if dp[m] == 10001:
    print(-1)
else:
    print(dp[m])


'''
책에서는 for j 를 돌릴때 money_type[i] 부터 m+1까지 돌렸다. 
그럴 필요없이 step을 money_type만큼 가져가게 
예를 들어 money_type이 2일때
2 4 6 8 10 이렇게 2 씩 증가하게 가져가면 더 효율적일것이다.
'''

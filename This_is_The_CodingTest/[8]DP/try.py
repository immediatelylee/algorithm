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

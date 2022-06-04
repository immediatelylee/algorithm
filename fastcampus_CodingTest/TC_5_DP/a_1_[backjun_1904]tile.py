n = int(input())

dp = [0 for _ in range(n+1)]

# fn = (fn-1 +1)  + (fn-2 +00)

dp[1] = 1
dp[2] = 2

for i in range(3, n+1):
    dp[i] = (dp[i-1] + dp[i-2]) % 15746

print(dp[n])

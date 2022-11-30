n = int(input())
storage = list(map(int, input().split()))

dp = [0 for _ in range(n+1)]

# ai = max(ai-2 +k, ai-1)
dp[0] = storage[0]
dp[1] = max(storage[0], storage[1])
for i in range(2, n):
    dp[i] = max(d[i-2]+storage[i], dp[i-1])

print(dp[n-1])

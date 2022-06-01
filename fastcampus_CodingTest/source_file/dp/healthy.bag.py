n, k = map(int, input().split())
dp = [[0] * (k+1) for _ in range(n + 1)]  # 가독성을 좋게 하기 위함

for i in range(1, n + 1):
    weight, value = map(int, input().split())
    # 1~K+1R까지 반복 // j는 무게의 합   dp[i][j]는 j일때 얻을 수 있는 최대 가치
    for j in range(1, k+1):
        if j < weight:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight] + value)

print(dp[n][k])

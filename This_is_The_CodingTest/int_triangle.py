


n = int(input())
dp = [[0 for _ in range(i)] for i in range(1, n+1)]

array = []

for i in range(n):
    array.append(list(map(int, input().split())))

if len(array) == 1:
    print(array[0][0])
else:
    dp[0] = int(array[0][0])
    dp[1][0] = int(array[1][0]) + int(array[0][0])
    dp[1][1] = int(array[1][1]) + int(array[0][0])

for i in range(2, n):
    for j in range(len(dp[i])):
        if j == 0:
            dp[i][j] = dp[i-1][j] + int(array[i][j])

        elif j == len(dp[i]) - 1:
            dp[i][j] = dp[i-1][j-1] + int(array[i][j])

        else:
            dp[i][j] = max(dp[i-1][j-1]+int(array[i][j]),
                           dp[i-1][j]+int(array[i][j]))

if len(array) != 1:
    print(max(dp[n-1]))

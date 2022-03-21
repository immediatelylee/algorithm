# 미완성 입력값도 인접행렬로 받을려고 했는데 정답 보니 그냥 한줄로 받고
# DP 에 계산해서 따로 저장함.

t = int(input())


for _ in range(t):
    n, m = map(int, input().split())

    gold_mine = [[] for _ in range(n)]
    input_gold = list(map(int, input().split()))
    dp = [[] for i in range(n)]

    for index, gold in enumerate(input_gold):

        gold_mine[index // m].append(gold)

    for j in range(1, m):
        for i in range(n):
            if i == 0:
                left_up = 0
            else:
                left_up = dp[i-1][j-1]

            if i == n-1:
                left_down = 0
            else:
                left_down = dp[i+1][j-1]

            left = dp[i][j-1]
            dp[i][j] = dp[i][j]+(max(left_up, left_down, left))
    result = 0
    for i in range(n):
        result = max(result, dp[i][m-1])

    print(result)

# https://www.acmicpc.net/problem/1495
# N,S,M == 곡의 개수,시작음량,최대음량
# 둘째줄에서는 곡마다 변경할수 있는 음량의 크기
# DP에 저장할거고  트리형으로 저장하려다가 일반DP로 저장해서 다시 품
N, S, M = map(int, input().split())
v_volumn = list(map(int, input().split()))
dp = [[0 for _ in range(M+1)] for _ in range(N+1)]
dp[0][S] = 1
for i in range(1, N+1):
    for j in range(M+1):
        if dp[i-1][j] == 0:
            continue
        if j-v_volumn[i-1] >= 0:
            dp[i][j-v_volumn[i-1]] = 1
        if j+v_volumn[i-1] <= M:
            dp[i][j+v_volumn[i-1]] = 1
result = -1
for i in range(M, -1, -1):
    if dp[N][i] == 1:
        result = i
        break
print(result)

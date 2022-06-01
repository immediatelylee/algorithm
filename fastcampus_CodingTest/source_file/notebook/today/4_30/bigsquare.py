# https://www.acmicpc.net/problem/1915

N, M = map(int, input().split())
A = [[0 for _ in range(M+1)] for i in range(N+1)]
# DP[i][j] = i,j 까지 왔을때 가장 큰 정사각형의 한변의 길이
# DP[i][j] = min(DP[i-1][j], DP[i-1][j-1], DP[i][j-1]) + 1
DP = [[0 for _ in range(M+1)] for i in range(N+1)]

for i in range(N):
    for idx, j in enumerate(list(map(int, list(input())))):
        A[i+1][idx+1] = j


# test A
# for i in A:
#     print(i)
# [0, 0, 0, 0, 0]
# [0, 0, 1, 0, 0]
# [0, 0, 1, 1, 1]
# [0, 1, 1, 1, 0]
# [0, 0, 0, 1, 0]

mx = 0

for i in range(1, N+1):
    for j in range(1, M+1):
        if A[i][j]:
            DP[i][j] = min(DP[i-1][j], DP[i-1][j-1], DP[i][j-1]) + 1

print(max([max(i) for i in DP]) ** 2)

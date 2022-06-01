# https://www.acmicpc.net/problem/11055
import copy
N, A = int(input()), list(map(int, input().split()))

# DP[i]: i까지 왔을때 합의 최대

DP = copy.deepcopy(A)

for i in range(1, N):
    for j in range(i):
        if A[i] > A[j]:
            DP[i] = max(A[i] + DP[j], DP[i])
            print(DP)
print(max(DP))

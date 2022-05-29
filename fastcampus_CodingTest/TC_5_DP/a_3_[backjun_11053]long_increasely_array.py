# https://www.acmicpc.net/problem/11053

N = int(input())

array = list(map(int, input().split()))
DP = [1] * N

for i in range(1, N):
    for j in range(0, i):
        if array[j] < array[i]:
            DP[i] = max(DP[i], DP[j]+1)

print(max(DP))

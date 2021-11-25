# https://www.acmicpc.net/problem/2167

# 첫째 줄에 배열의 크기 N, M(1 ≤ N, M ≤ 300)이 주어진다. 다음 N개의 줄에는 M개의 정수로 배열이 주어진다.
# 배열에 포함되어 있는 수는 절댓값이 10,000보다 작거나 같은 정수이다. 그 다음 줄에는 합을 구할 부분의 개수 K(1 ≤ K ≤ 10,000)가 주어진다.
# 다음 K개의 줄에는 네 개의 정수로 i, j, x, y가 주어진다(i ≤ x, j ≤ y).
# 시간복잡도 300*300 * 쿼리(10000) -> 9억  파이썬으로는 힘들다.
# 누적합을 써야 한다.


# 1차원 누적합
# A = [i for i in range(10)]

# print(A)
# for i in range(1, 10):
#     A[i] = A[i-1] + A[i]

# print(A)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# [0, 1, 3, 6, 10, 15, 21, 28, 36, 45]

# 누적합의 활용
# DP[i] = i까지 합
# i부터 j까지의 합은 DP[i] - DP[j-1]
# 시간복잡도 O(N)

# 2차원 배열의 누적합
# 1 2 4
# 8 16 32
# 이라고 한다면 1 2 8 16 의 누적합  27을 얻고자 하는데 누적합끼리 더하면 1 +2 = 3 ,  1 +8 = 9 , 3+9+ 16 = 28
# 윗쪽에서 온 누적합이랑 겹치는 부분 대각선 위에 부분이 중첩됨
# 왼쪽 윗쪽 누적합을 더하고 대각선 부분을 빼야함.
# A [0:0] = 10  이런 식의 문법은 파이썬에서안됨
# 왜 0 인덱스에 집착하느냐는 대각선을 구할때 0인덱스가 안되면 까다롭기 때문

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
DP = [[0 for i in range(M+1)] for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, M+1):
        DP[i][j] = DP[i-1][j] + DP[i][j-1] - DP[i-1][j-1] + A[i-1][j-1]

# Test DP
# for i in DP:
#     print(i)


for _ in range(int(input())):
    i, j, x, y = map(int, input().split())
    print(DP[x][y] - DP[i-1][y] - DP[x][j-1] + DP[i-1][j-1])

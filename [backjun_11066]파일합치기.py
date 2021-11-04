# https://www.acmicpc.net/problem/11066

def process():
    N, A = int(input()), [0] + list(map(int, input().split()))
    # S[i]는 1번부터 i번까지의 누적합
    # A = [0] + A 의 식은 시간복잡도가 좀 올라가긴하지만 구현하기는 쉽다.
    S = [0 for _ in range(N+1)]
    for i in range(1, N+1):
        S[i] = S[i-1] + A[i]

    # DP[i][j] : i에서 j까지 합하는데 필요한 최소 비용
    # DP[i][k] + DP[k+1][j] + sum(A[i]~A[j])
    DP = [[0 for i in range(N+1)] for _ in range(N+1)]
    for i in range(2, N+1):  # 부분파일의 길이
        # 시작점  # j가 N+1 인데 N크기의 부분집합을 구할수 없기 떄문에 i를 빼준다.
        for j in range(1, N+2-i):
            DP[j][j+i-1] = min([DP[j][j+k] + DP[j+k+1][j+i-1]
                                for k in range(i-1)]) + S[j+i-1] - S[j-1]
    # DP test
    # for i in DP:
    #     print(i)
    print(DP[1][N])


for _ in range(int(input())):
    process()

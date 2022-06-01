# https://www.acmicpc.net/problem/1012
# flood fill 문제
# 재귀함수가 너무 깊이 내려가면 터져버림.
import sys
sys.setrecursionlimit(10000)

T = int(input())
B, ck = [], []

dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]


def dfs(x, y):
    global B, ck
    # if ck[x][y]:   무한반복
    #     return
    ck[x][y] = 1
    for i in range(4):
        xx, yy = x+dx[i], dy[i]
        if B[xx][yy] == 0 or ck[xx][yy]:
            continue
        dfs(xx, yy)


def process():
    global B, ck  # 안쓰면 indexerror 가 뜸
    M, N, K = map(int, input().split())
    B = [[0 for i in range(M)] for _ in range(N+2)]
    for _ in range(K):
        X, Y = map(int, input().split())
        B[Y+1][X+1] = 1  # 첫 위치를 1로 잡고 나머지를 0으로 지정한다.
    ans = 0

    # flood fill 은 어디가 차있는지 모르기 때문에 전수 조사하고 체크된것은 조사하지 말하야 한다.
    # 그래서 flood fill 의 시간 복잡도는 맵의 크기이다.
    for i in range(1, M+1):
        for j in range(1, M+1):
            if B[i][j] == 0 or ck[i][j]:
                continue
            dfs(i, j)
            ans += 1
    print(ans)


for _ in range(T):
    process()

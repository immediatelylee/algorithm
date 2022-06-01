import sys
sys.setrecursionlimit(10000)

T = int(input())
B, ck = [], []

dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]


def dfs(x, y):
    global B, ck
    if ck[x][y] == 1:
        return
    ck[x][y] = 1
    for i in range(4):
        xx, yy = x+dx[i], y+dy[i]
        if B[xx][yy] == 0 or ck[xx][yy]:
            continue
        dfs(xx, yy)


def process():
    global B, ck
    M, N, K = map(int, input().split())
    B = [[0 for i in range(50+2)] for _ in range(50+2)]
    ck = [[0 for i in range(50+2)] for _ in range(50+2)]
    for _ in range(K):
        X, Y = map(int, input().splilt())
        B[Y+1][X+1] = 1
    ans = 0
    for i in range(1, N+1):
        for j in range(1, M+1):
            if B[i][j] == 0 or ck[i][j]:
                continue
            dfs(i, j)
            ans += 1
    print(ans)


for _ in range(T):
    process()
# flood fill 은 반드시 전수조사를 한번해야 한다.
# 어느것이 차있는지 모르기 때문 대신 탐색한 부분은 다시 탐색하지 않는다.

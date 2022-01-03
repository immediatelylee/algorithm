N, M = map(int, input().split())
check = [[0]*M for i in range(N)]
drink = [list(map(int, input().split())) for i in range(N)]


def dfs(x, y):
    if x < 0 or y < 0 or x > N or y > M:
        return False
    if check[x, y] == 1 or drink[x][y] == 1:
        return False
    check[x][y] = 1
    dfs(x-1, y)
    dfs(x+1, y)
    dfs(x, y-1)
    dfs(x, y+1)

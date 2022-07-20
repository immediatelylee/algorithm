from timeit import default_timer as timer
from datetime import timedelta


N, M = map(int, input().split())
check = [[0]*M for i in range(N)]
drink = [list(map(int, input())) for i in range(N)]

count = 0
start = timer()


def dfs(x, y):  # list out of range주의
    if x < 0 or y < 0 or x > N-1 or y > M-1:
        return False
    elif check[x][y] == 1 or drink[x][y] == 1:
        return False
    check[x][y] = 1
    dfs(x-1, y)
    dfs(x+1, y)
    dfs(x, y-1)
    dfs(x, y+1)

    return True


for i in range(N):
    for j in range(M):
        if dfs(i, j):
            count += 1

print(count)
end = timer()
print(timedelta(seconds=end-start))
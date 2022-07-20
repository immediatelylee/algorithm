'''
DFS 활용 
dxdy를 하지 않고 dfs를 만들고 상하좌우에 해당하는 x,y값을 입력하여 처리 
마지막에는 cnt1을 해주어 갯수를 센다.
'''


n, m = map(int, input().split())
map_data = []
for i in range(n):
    map_data.append(list(input()))


def dfs(x, y):
    if x < 0 or y < 0 or x >= n or y >= m or map_data[x][y] == '1':
        return

    map_data[x][y] = '1'
    dfs(x-1, y)
    dfs(x+1, y)
    dfs(x, y-1)
    dfs(x, y+1)


cnt = 0
for i in range(n):
    for j in range(m):
        if map_data[i][j] == '0':
            dfs(i, j)
            cnt += 1

print(cnt)

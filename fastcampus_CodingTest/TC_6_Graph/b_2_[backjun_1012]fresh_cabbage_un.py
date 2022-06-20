# https://www.acmicpc.net/problem/1012

t= int(int(input()))
m,n,k = map(int,input().split())
cabbage = [[0 for _ in range(m)] for _ in range(n)]
count = 0
check = [[0 for _ in range(m)] for _ in range(n)]

dx=[-1,1,0,0]
dy = [0,0,1,-1]

def dfs(x, y):
    if x < 0 or y < 0 or x >= n or y >= m or cabbage[x][y] == '0' :
        return

    map_data[x][y] = '1'
    dfs(x-1, y)
    dfs(x+1, y)
    dfs(x, y-1)
    dfs(x, y+1)



for _ in range(k):
    xx,yy = map(int,input().split())
    gabbage[xx][yy]=1
    check[xx][yy]=1
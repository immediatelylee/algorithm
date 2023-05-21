'''
음료수 열러먹기 [][][]
    dx,dy없이
    dx,dy사용해서 
미로탈출       [][][]


'''


n,m =map(int,input().split())
graph = []

dx = [-1,0,1,0]
dy = [0,1,0,-1]


for i in range(n):
    graph.append(list(map(int,input())))

def dfs(x,y):
    if x <0 or y<0 or x >= n or y >= m:
        return False
    if graph[x][y] ==0:
        graph[x][y] =1

        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True
    return False


result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result +=1

print(result)
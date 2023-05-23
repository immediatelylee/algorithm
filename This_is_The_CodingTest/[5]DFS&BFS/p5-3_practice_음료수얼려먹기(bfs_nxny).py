from collections import deque

n,m =map(int,input().split())
graph = []

dx = [-1,0,1,0]
dy = [0,1,0,-1]


for i in range(n):
    graph.append(list(map(int,input())))

def dfs(x,y):
    if graph[x][y] ==1:
        return False
    queue = deque()
    queue.append((x,y))

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx <0 or ny<0 or nx >= n or ny >= m:
                    continue
            if graph[nx][ny] ==0:
                graph[nx][ny] =1
                queue.append((nx,ny))

    return 1
                
            


result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == 1:
            result +=1

print(result)

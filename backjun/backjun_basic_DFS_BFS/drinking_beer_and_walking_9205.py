# https://www.acmicpc.net/problem/9205

from collections import deque

# 1000 거리 안에 있으면 while문을 게속 돌림 
# nx,ny와 x,y의 거리 차가 1000 이내라면 방문하고 q에 넣고
def bfs():
    q= deque()
    q.append([home[0],home[1]])
    while q:
        x,y =q.popleft()
        if abs(x - festival[0]) + abs(y-festival[1]) <= 1000:
            print("happy")
            return
        for i in range(n):
            if not visited[i]:
                nx,ny = cs[i]
                if abs(x - nx) + abs(y - ny)<= 1000:
                    q.append([nx,ny])
                    visited[i] =1
    print("sad")
    return

t = int(input())
for i in range(t):
    n = int(input())
    home =[int(x) for x in input().split()]
    cs = []
    for j in range(n):
        x,y = map(int,input().split())
        cs.append([x,y])
    festival = [int(x) for x in input().split()]
    visited = [0 for i in range(n+1)]
    bfs()

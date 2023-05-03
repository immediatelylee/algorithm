'''
특정거리 도시찾기 [v][x][]


'''
from collections import deque

graph =[ [] for i in range(n+1)]
n,m,k,x = map(int,input().split())
distance = [ -1 for i in range(n+1)]

for i in range(n):
    x,y = map(int,input().split())
    graph[x].append(y)


q = deque()
q.append(x)
while q:
    q.popleft()

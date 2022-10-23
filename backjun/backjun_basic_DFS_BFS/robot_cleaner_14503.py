from collections import deque

n,m = map(int,input().split())
dirtyroom = []
r,c,d = map(int,input().split())

for _ in range(n):
    dirtyroom.append(list(list(map(int,input().split()))))

direction = {0:(0,-1),1:(1,0),2:(-1,0),3:(0,1)}




def bfs(x,y):
    q = deque()
    q.append((x,y))

    while q:
        x,y = q.popleft()
        



def turn_left_90degree(x,y):
    
    pass
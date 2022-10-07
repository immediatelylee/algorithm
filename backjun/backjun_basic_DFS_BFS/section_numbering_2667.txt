from collections import deque

n = int(input())

section_map = []
for _ in range(n):
    section_map.append(list(map(int,input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer =[]


def bfs(x,y):
    q = deque()
    q.append((x,y))
    section_map[x][y] = 0
    cnt = 1

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n and section_map[nx][ny] == 1:
                section_map[nx][ny] = 0
                q.append((nx, ny))
                cnt+=1
    
    return cnt

for i in range(n):
    for j in range(n):
        if section_map[i][j] == 1:
            answer.append(bfs(i,j))

answer.sort()
print(len(answer))
for i in answer:
    print(i)



  
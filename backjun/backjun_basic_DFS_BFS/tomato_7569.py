# https://www.acmicpc.net/problem/7569
from collections import deque

m, n, h = map(int, input().split())

box = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]


visited = [[0] * (n*h)]

dx = [-1, 0, 1, 0, 0, 0]
dy = [0, 1, 0, -1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

que = deque()
cnt = 0


def bfs():
    while que:
        z, x, y = que.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if -1 < nx < n and -1 < ny < m and -1 < nz < h:
                if box[nz][nx][ny] == 0:
                    box[nz][nx][ny] = box[z][x][y]+1
                    que.append((nz, nx, ny))


for i in range(h):
    for j in range(n):
        for k in range(m):
            if box[i][j][k] == 1:
                que.append((i, j, k))


# bfs 다 돌렸는데도 익지 않은 토마토가 있다면 flag =1 으로 구별
# result가 -2 인데 max 값이 -1 이라면 전 맵에 -1 만 있는것으로 간주한다.
# 토마토가 모두 익지는 못하는 상황이면 -1을 출력해야 한다.
# 만약, 저장될 때부터 모든 토마토가 익어있는 상태이면 0을 출력해야 하고
bfs()
flag = 0
result = -2
for i in range(h):
    for j in range(n):
        for k in range(m):
            # 높이, x,y 순서
            if box[i][j][k] == 0:  # 익지 않은 토마토가 있는 경우
                flag = 1
                # 높이, x,y 순서
            result = max(result, box[i][j][k])
if flag == 1:  # 토마토가 0 익지 않은 토마토가 있다 - 모든 토마토가 익을수 없는 상태  -> -1
    print(-1)
# elif result == -1:
#     print(0)
else:
    print(result-1)

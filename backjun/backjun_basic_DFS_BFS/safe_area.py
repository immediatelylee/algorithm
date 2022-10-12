# https://www.acmicpc.net/problem/2468
from collections import deque

n = int(input())
data = []
maxnum = 0

for i in range(n):
    data.append(list(map(int, input().split())))
for i in range(n):
    maxnum = max(maxnum, max(data[i]))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(a, b, value, visited):
    q = deque()
    q.append((a, b))
    visited[a][b] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if data[nx][ny] > value and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append((nx, ny))


result = 0
for i in range(maxnum):
    visited = [[0] * n for i in range(n)]
    cnt = 0

    for j in range(n):
        for k in range(n):
            if data[j][k] > i and visited[j][k] == 0:
                bfs(j, k, i, visited)
                cnt += 1

    if result < cnt:
        result = cnt

print(result)

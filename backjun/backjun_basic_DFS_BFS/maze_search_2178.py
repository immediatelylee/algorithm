# https://www.acmicpc.net/problem/2178
# 이것이 코딩테스트다 5-11번문제와 동일한것 같다. 답안이
from collections import deque
n, m = map(int, input().split())
map_data = []

for i in range(n):
    map_data.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m or map_data[nx][ny] == 0:
                continue
            if map_data[nx][ny] == 1:
                map_data[nx][ny] = map_data[x][y]+1
                queue.append((nx, ny))
    return map_data[n-1][m-1]


print(bfs(0, 0))

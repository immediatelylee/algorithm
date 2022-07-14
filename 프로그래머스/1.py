from collections import deque
import sys

input = sys.stdin.readline

n, m, v = map(int, input().split())
# 인접 행렬 초기화.
graph = [[0] * (n+1) for _ in range(n+1)]
# 인접행렬에 데이터 입력
for _ in range(m):
    line = list(map(int, input().split()))
    graph[line[0]][line[1]] = 1
    graph[line[1]][line[0]] = 1


def dfs(start, visited):
    visited += [start]
    for c in range(len(graph[start])):
        if graph[start][c] == 1 and (c not in visited):
            dfs(c, visited)
    return visited


def bfs(start):
    visited = [start]
    queue = [start]
    while queue:
        n = queue.pop(0)
        for c in range(len(graph[start])):
            if graph[n][c] == 1 and (c not in visited):
                visited.append(c)
                queue.append(c)
    return visited


print(*dfs(v, []))
print(*bfs(v))

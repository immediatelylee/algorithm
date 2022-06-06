from collections import deque

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
queue = deque([])

for _ in range(m):
    start, end = map(int, input().split())
    graph[start].append((start, end))


def DFS(start, end):


DFS(v)

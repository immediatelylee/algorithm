import sys
from collections import deque

# N: 노드 수 / M: 간선 수 / V: 탐색 시작 지점
N, M, V = map(int, sys.stdin.readline().split(" "))

# 인접 리스트
adj = [[] for _ in range(N)]
visited = [1 for _ in range(N)]

# 인접 리스트에 추가
for _ in range(M):
    x, y = map(int, sys.stdin.readline().split(" "))
    adj[x-1].append(y-1)
    adj[y-1].append(x-1)


# dfs
stack = []
dfs = []
stack.append(V-1)

for each in adj:
    each.sort(reverse=True)

while stack:
    v = stack.pop()
    if visited[v] == 1:
        dfs.append(v)
        visited[v] = 0

    for each in adj[v]:
        if visited[each] == 1:
            stack.append(each)

for i in range(len(dfs)):
    if i == len(dfs)-1:
        print(dfs[i]+1)
    else:
        print(dfs[i]+1, end=' ')


# bfs
queue = deque()
bfs = []

for each in adj:
    each.sort()

# 시작점
queue.append(V-1)
visited[V-1] = 1

while queue:
    v = queue.popleft()
    bfs.append(v)

    for each in adj[v]:
        if visited[each] == 0:
            queue.append(each)
            visited[each] = 1

for i in range(len(bfs)):
    if i == len(bfs)-1:
        print(bfs[i]+1)
    else:
        print(bfs[i]+1, end=' ')

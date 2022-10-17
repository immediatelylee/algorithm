from collections import deque

n, m, v = map(int, input().split())
data = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]


for _ in range(m):

    x, y = map(int, input().split())
    data[x].append(y)
    data[y].append(x)

for i in range(len(data)):
    data[i].sort()


result = []
result1 = []


def dfs(v):
    visited[v] = 1
    result.append(v)
    for i in data[v]:
        if not visited[i]:
            visited[i] = 1
            dfs(i)

# 큐 넣는거 잊지 말기


def bfs(v):
    visited = [0 for _ in range(n+1)]
    visited[v] = 1
    result1.append(v)
    q = deque([v])
    while q:
        t = q.popleft()
        for i in data[t]:
            if not visited[i]:
                result1.append(i)
                q.append(i)
                visited[i] = 1


dfs(v)
bfs(v)
# *[] 은 unpacking
print(*result)
print(*result1)

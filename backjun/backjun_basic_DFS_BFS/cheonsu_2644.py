n = int(input())
x, y = map(int, input().split())
graph = [[] for _ in range(n+1)]
m = int(input())
visited = [False] * (n+1)
result = []

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(v, num):
    num += 1
    visited[v] = True

    if v == y:
        result.append(num)

    for i in graph[v]:
        if not visited[i]:
            dfs(i, num)


dfs(x, 0)
if len(result) == 0:
    print(-1)
else:
    print(result[0]-1)

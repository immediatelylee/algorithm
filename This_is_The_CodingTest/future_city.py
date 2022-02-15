n, m = map(int, input().split())

graph = [[] for i in range(n+1)]

for i in range(1, m+1):
    x, y = map(int, input().split())
    graph[x].append(y)

print(graph)

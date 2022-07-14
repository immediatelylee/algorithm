import sys
input = sys.stdin.readline
n, m, v = map(int, input().split())
graph = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    line = list(map(int, input().split()))
    graph[line[0]][line[1]] = 1
    graph[line[1]][line[0]] = 1


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


def dfs(start, visited):
    visited += [start]
    print("[visited]:", visited)
    # graph[1] 이 들어가면 graph[1][1],graph[1][2],graph[1][3].... 출력
    for c in range(len(graph[start])):
        # graph[start]= [0,0,1,1,1]
        print(len(graph[start]), graph[start])
        print("c:", c)
        if graph[start][c] == 1 and (c not in visited):
            if graph[start][c] == 1 and (c not in visited):
                print("dfs")
                dfs(c, visited)
    return visited


print(*dfs(v, []))
print(*bfs(v))

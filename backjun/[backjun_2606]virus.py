# https://www.acmicpc.net/problem/2606
# pc수가 적으므로 dfs가 간편하다.
# 시작하는 정점은 빼야하므로 1을뺀다. 

n = int(input())
c = int(input())
adj = [[] for _ in range(n+1)]
visited = [False] * (n+1)
count = 0

for _ in range(c):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)


def dfs(now_pos):
    global count
    count += 1
    visited[now_pos] = True
    for next_pos in adj[now_pos]:
        if not visited[next_pos]:
            dfs(next_pos)


dfs(1)
print(count - 1)

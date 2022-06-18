# https://www.acmicpc.net/problem/2606
# pc수가 적으므로 dfs가 간편하다.
# 시작하는 정점은 빼야하므로 1을뺀다.

from collections import deque
import sys

sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")

# inputdata
# 7
# 6
# 1 2
# 2 3
# 1 5
# 5 2
# 5 6
# 4 7
# -> 4

n = int(input())
c = int(input())
count = 0
adj = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(c):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)


def bfs(v):
    global count
    q = deque([v])
    while q:
        v = q.popleft()
        if not(visited[v]):
            visited[v] = True
            count += 1
            for e in adj[v]:
                if not visited[e]:
                    q.append(e)


def dfs(now_pos):
    global count
    count += 1
    visited[now_pos] = True
    for next_pos in adj[now_pos]:
        if not visited[next_pos]:
            dfs(next_pos)


bfs(1)
# dfs(1)
print(count - 1)

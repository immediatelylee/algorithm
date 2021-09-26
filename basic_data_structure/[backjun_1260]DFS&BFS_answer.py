# https://www.acmicpc.net/problem/1260

from collections import deque


def dfs(v):
    print(v, end=' ')
    visited[v] = True
    for e in adj[v]:
        if not(visited[e]):
            dfs(e)


def bfs(v):
    q = deque([v])
    while q:
        v = q.popleft()
        if not(visited[v]):
            visited[v] = True
            print(v, end=' ')
            for e in adj[v]:
                if not visited[e]:
                    q.append(e)


n, m, v = map(int, input().split())
adj = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)
for e in adj:
    e.sort()

visited = [False] * (n + 1)
dfs(v)
print()
visited = [False] * (n + 1)
bfs(v)
# need_visit,visited 두개의 큐를 생성해야함.
# 시간 복잡도는 둘다 O(V+E)
# 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다.
# 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.
# 입력
# 4 5 1
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4
# 출력
# 1 2 4 3
# 1 2 3 4
# 입력
# 1000 1 1000
# 999 1000
# 출력
# 1000 999
# 1000 999

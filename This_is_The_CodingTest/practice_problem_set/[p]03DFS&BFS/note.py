'''
특정거리 도시찾기 [][][]


'''

from collections import deque
n, m, k, x = map(int, input().split())

data = [[] for _ in range(n+1)]
visit = [[False] for _ in range(n+1)]

for i in range(m):
    x, y = map(int, input().split())
    data[x].append(y)

# 모든 도시에 대한 최단 거리 초기화 !!
distance = [-1] * (n+1)
distance[x] = 0

q = deque([x])
while q:
    now = q.popleft()
    for next_node in data[now]:
        if distance[next_node] == -1:
            distance[next_node] = distance[now] + 1
            q.append(next_node)

check = False
for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        check = True

if check == False:
    print(-1)

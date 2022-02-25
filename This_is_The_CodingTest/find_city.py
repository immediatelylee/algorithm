from collections import deque
# n은 도시개수 m은 도로의 개수,k는 거리정보,x는 출발도시의 번호
n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]

for i in range(m):
    s, d = map(int, input().split())
    graph[s].append(d)

# 모든 도시에 대한 최단 거리 초기화
distance = [-1]*(n+1)
distance[x] = 0

q = deque([x])
while q:
    now = q.popleft()
    for next_node in graph[now]:
        if distance[next_node] == -1:
            distance[next_node] = distance[now]+1
            q.append(next_node)

# 최단 거리가 k인 모든 도시의 번호를 오름차순으로 출력
check = False
for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        check = True

if check == False:
    print(-1)

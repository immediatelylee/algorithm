import heapq
import sys

input = sys.stdin.readline

INF = int(1e9)
n, m, start = map(int, input().split())
graph = [[] for i in range(n+1)]
distance = [INF]*(n+1)

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        # 1 2 4 -> [1]=[(2,4)]  dist =2 now = 4
        dist, now = heapq.heappop(q)
        # dist는 뭐지? heapq.heappop(q)를 한 첫번째 값 거리값 ,  now 는 현재 노드에 대한 값
        # distance[now] now번째 노드의 최소거리 , 현재 노드 최소거리값보다 큐에서 나온 값이 크면 건너뛰기
        # 거리 테이블의 값이 큐에서 나온값보다 작다면 이미 처리된것으로 간주한다.
        if distance[now] < dist:
            continue

        # (2,4) ,(3,2) 나중에 graph[2] ,graph[3]도 탐색하는데 빈 리스트여서 바로 올라감.
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:  # cost가 distance[i[0]] 목적지의 distance보다 작으면
                distance[i[0]] = cost  # 변경
                heapq.heappush(q, (cost, i[0]))  # [(4,2)] ->  (2,3),(4,2)


dijkstra(start)

count = 0
max_distance = 0
for d in distance:
    if d != INF:
        count += 1
        max_distance = max(max_distance, d)

print(count - 1, max_distance)

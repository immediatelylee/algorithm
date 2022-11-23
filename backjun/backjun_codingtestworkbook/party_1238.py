# https://www.acmicpc.net/problem/1238
import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

v, e, x = map(int, input().split())

graph = [[] for _ in range(v + 1)]

for _ in range(e):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))


def dijkstra(start):
    q = []
    # dijkstra를 여러번 해야 하므로 초기화를 함수 안에 넣는다.
    distance = [INF] * (v + 1)
    # 입력할때와 다르게 거꾸로 넣는다 heapq최소힙에 넣어서 뽑아야 하므로
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue

        for node_index, node_cost in graph[now]:
            cost = dist + node_cost

            if distance[node_index] > cost:
                distance[node_index] = cost
                heapq.heappush(q, (cost, node_index))
    # 시작점이 start인 전체 거리 리스트를 반환
    return distance


result = 0
for i in range(1, v + 1):
    # dijkstra(시작점) -> 시작점으로부터 갈수 있는 노드의 거리 리스트 반환
    go = dijkstra(i)
    back = dijkstra(x)
    result = max(result, go[x] + back[i])

print(result)

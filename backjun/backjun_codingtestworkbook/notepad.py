import heapq

n, m, x = map(int, input().split())
INF = int(1e9)
graph = [[] for _ in range(n+1)]


for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def dijkstra(start):
    q = []
    # dijkstra를 여러번 해야 하므로 초기화를 함수 안에 넣는다.
    distance = [INF]*(n+1)
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

            if cost < distance[node_index]:
                distance[node_index] = cost
                heapq.heappush(q, (cost, node_index))
    # 시작점이 start인 전체 거리 리스트를 반환
    return distance


result = 0
for i in range(1, n+1):
    # dijkstra(시작점) -> 시작점으로부터 갈수 있는 노드의 거리 리스트 반환
    go = dijkstra(i)
    back = dijkstra(x)
    result = max(result, go[x]+back[i])

print(result)

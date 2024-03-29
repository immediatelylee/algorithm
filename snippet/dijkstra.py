import heapq

# sys.stdin.readline() 이란 파이썬 내장 함수로 input()을 치환하면,
# 입력 데이터 수가 많아도 빠르게 동작 가능하다.
import sys
input = sys.stdin.readline
INF = int(1e9)  # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수, 간선의 개수 입력받기
n, m = map(int, input().split())
# 시작 노드 번호를 입력받기
start = int(input())
# 각 노드에 연결된 노드에 대한 정보를 담는 리스트 생성
graph = [[] for i in range(n+1)]
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c
    graph[a].append((b, c))


def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    # 여기서 cost,index순으로 넣는다 최소힙을 쓸거기 때문에
    heapq.heappush(q, (0, start))
    # heappush (입력할 대상리스트,추가할원소)
    distance[start] = 0
    while q:  # 큐가 비어있지 않다면
        # 최단 거리가 가장 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for node_index, node_cost in graph[now]:
            cost = dist + node_cost
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[node_index]:
                distance[node_index] = cost
                # 최소 힙을 써야 하기 때문에 cost,index순으로 넣는다.
                heapq.heappush(q, (cost, node_index))


# 다익스트라 알고리즘을 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n+1):
    # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
    if distance[i] == INF:
        print("INFINITY")
    # 도달할 수 있는 경우, 거리를 출력
    else:
        print(distance[i])

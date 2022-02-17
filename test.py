# 다익스트라 알고리즘

# 최단거리를 구하기 위한 알고리즘이다
# 시작점으로 부터 최단거리의 노드에 방문하여 경로의 최소비용을 계산하여 저장한다. 그래서 마지막 노드까지 갱신하면 최소비용만 저장된 것이 리스트로 남는다.
# 기존의 방법과 최소힙을 이용한 방법이 있다.
# 기존의 방법에는 최소거리의 노드를 찾기 위한 함수가 필요하며 각 노드 마다 전체 검색을 하기 떄문에 시간 알고리즘은 (v^2) 이다 v개  v번 탐색
# 최소힙을 사용한 개선된 알고리즘에는 이런 전체 탐색을 하는 부분의 시간이 줄게 된다 최소힙에 넣게 되면 최소값을 갖는 것이 head로 올라오기 때문
# 시간 복잡도는 Elogv 가 된다.
#

import heapq
# 입력값 n,m
n, m = map(int, input().split())
# 초기값 start
start = int(input())

# 초기화
graph = [[] for i in range(n+1)]  # n+1개를 받아야함
INF = int(1e9)
distance = [[INF] for i in range(n+1)]  # n+1개를 받아야함

# graph정보 저장
# a는 출발지 b는 도착지 c는 거리
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def dijkstra():
    # 시동 코드
    # 1. q 생성하고
    # 2. 시작노드로 가기 위한 최단 거리는 0으로 설정
    # (heap으로 q에다가 0,start를 넣고 출발 distance에다가 0)
    q = []
    # 큐에 (0,start)를 push함 거리 0, 노드 가 1 의 비용  기존 다익스트라랑 다름  heapq를 이용하기 때문이다.
    heapq.heappush(q, (0, start))
    distance[start] = 0

    # 큐가 있을때 최소거리의 노드에 방문해서 갱신해야 함.
    while q:

        dist, now = heapq.heappush(q)  # 최소거리 노드정보 출력
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            distance[i[0]] = cost
            heapq.heappush(q, (cost, i[0]))

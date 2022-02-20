from collections import deque

v, e = map(int, input().split())

indegree = [0] * (v+1)

graph = [[] for i in range(v+1)]

# 방향그래프의 모든 간선 정보를 입력 받기
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)  # 정점 A에서 B 이동 가능
    # 진입 차수를 1증가
    indegree[b] += 1


def topology_sort():
    result = []
    q = deque()
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)

    # 진입차수가 0인 원소와 연결된 노드들의 진입차수에서 1빼기
    while q:
        now = q.popleft()
        result.append(now)

        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    for i in result:
        print(i, end=' ')


topology_sort()

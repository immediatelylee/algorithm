# https://www.acmicpc.net/problem/1260
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

def bfs(graph, start_node):
    visited = list()
    need_visit = list()
    need_visit.append(start_node)
    while need_visit:
        node = need_visit.pop(0)
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])
    return visited


def dfs(graph, start_node):
    visited, need_visit = list(), list()
    need_visit.append(start_node)

    while need_visit:
        node = need_visit.pop()
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])

    return visited


N, M, V = map(int, input().split())
graph = dict()

for _ in range(M):
    key, value = map(int, input().split())
    graph[key]
print(graph)

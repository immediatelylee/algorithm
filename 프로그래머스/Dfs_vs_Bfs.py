# Dfs 깊이 우선탐색이라 부르며 그래프에서 깊은부분을 우선적으로 탐색하는 알고리즘
# 1. 탐사시작노드를 스택에 삽입하고 방문처리를 한다.
# 2. 스택의 최상단 노드에 방문하지 않은 인접 노드가 있으면 그 인접 노드를 스택에 넣고 방문처리를 한다.
# 2-1. 방문하지 않은 인접노드가 없으면 스택에서 최상단 노드를 꺼낸다.
# 3.2번의 과정을 더이상 수행할 수 없을 때까지 반복한다.

# Bfs 너비우선탐색이라 부르며 가까운 노드부터 탐색하는 알고리즘이다.
# Bfs 구현에는 선입선출 방식인 큐 자료구조를 이용하는 것이 정석이다.
# 1. 탐색노드를 큐에 삽입하고 방문 처리를 한다.
# 2. 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리를 한다.

# [중요]정점의 n 을 이용하여 n+1의 인접 행렬의미는
# 인접 행렬이 정점마다 만날수 있는 모든경우의 수를 담게 행렬로 표시한것이며
# 행과 열에 [0]을 사용하지 않기에 n+1 dlek.

# bfs
from collections import deque
a, b, v = map(int, input().split())
graph = []
for i in range(b):
    input_data = list(map(int, input().split()))
    graph.append(input_data)
    print(graph)

visited = [False] * 9


def dfs(graph, v, visited):
    # 현재의 노드를 방문처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


dfs(graph, v, visited)

visited = [False] * 9
start = v


def bfs(graph, start, visited):
    # 큐 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때 까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')
        # 해당 원소와 연결된 , 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


bfs(graph, start, visited)

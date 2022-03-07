from collections import deque


def bfs(graph, start, visited):

    queue = deque([start])
    # 현재 노드 방문처리
    visited[start] = True
    # 큐가 빌때 까지 반복
    while queue:
        # 큐에서 원소 하나를 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')
        # 해당 원소와 연결된 , 아직 방문하지 않은 원소들을 큐에 삽입

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


graph = ["그래프값 입력"]

visited = [False] * 9  # 그래프 원소의 개수
# 정의된 BFS함수 호출
bfs(graph, 1, visited)

# BFS활용 1 미로탈출

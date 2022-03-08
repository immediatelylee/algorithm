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
# 1. 큐 선언  start를 큐에 넣고 while문
# 2. while문 큐가 빌때 까지 반복
# 3. 똑같이 popleft해서 추출하고  방향벡터 선언한거로 nx,ny를 만들어서 예외사항 체크
# 4. 예외사항 통과하면 graph[nx][ny] 에 +1 (거리를 구하는 거이므로)
# 5. 그리고 다시 큐에 넣는다. 반복해서 graph를 채운다.  이건ㄴ visit을 따로 만들지 않고 graph에 수치값을 게속 추가하는 방식으로 진행함.

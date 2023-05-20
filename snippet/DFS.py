def DFS(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            DFS(graph, i, visited)


graph = ["그래프값 입력"]
visited = [False] * 9  # 노드의 개수
DFS(graph, 1, visited)

# 활용1 음료수 얼리기
# 1. 맵입력받고
# 2. dfs 에 예외조건이면 return  아니면 방문처리 후 상하좌우로 dfs
# 3. for문 돌려서 0의 덩어리 확인후 count +1  (dfs로 덩어리 찾기)

# 상하좌우 진행용 방향 리스트
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 아이스크림 개수
count = 0

# dfs를 통해 현재 노드를 방문한 뒤, 연결된 모든 노드들을 방문


def dfs(start_x, start_y):

    # 현재 노드를 방문 처리
    ice_board[start_x][start_y] = 1

    # 현재 노드와 인접한 모든 노드들을 탐색하며, 방문 가능할 경우 방문
    for i in range(4):

        # 인접 노드 좌표
        nx = start_x + dx[i]
        ny = start_y + dy[i]

        # 인접 노드가 얼음판 내부에 위치할 경우
        if (nx >= 0 and nx < n and ny >= 0 and ny < m):

            # 인접 노드에 음료수를 채울 수 있는지 확인
            if (ice_board[nx][ny] == 0):

                # 인접 노드 방문
                dfs(nx, ny)
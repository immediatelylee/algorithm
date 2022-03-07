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

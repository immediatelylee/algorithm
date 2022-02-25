from collections import deque
n, k = map(int, input().split())

virus_map = []  # 전체 보드 정보
data = []  # 바이러스에 대한 정보를 담는 리스트
for i in range(n):
    virus_map.append(list(map(int, input().split())))
    for j in range(n):
        # 해당 위치에 바이러스가 존재하는 경우
        if virus_map[i][j] != 0:
            # (바이러스 종류, 시간,위치 x,위치 y) 삽입
            data.append((virus_map[i][j], 0, i, j))

# 정렬 이후에 큐로 옮기기(낮은 번호의 바이러스가 먼저 증식하므로)
data.sort()
q = deque(data)

target_s, target_x, target_y = map(int, input().split())


# 바이러스는 상하좌우로 퍼짐.
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 너비 우선 탐색 진행
while q:
    virus, s, x, y = q.popleft()
    # 정확히 s초가 지나거나,큐가 빌때 까지 반복
    if s == target_s:
        break
    # 현재 노드에서 주변 4가지 위치를 각각 확인
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx and nx < n and 0 <= ny and ny < n:
            # 아직 방문하지 않은 위치라면, 그 위치에 바이러스 넣기
            if virus[nx][ny] == 0:
                virus_map[nx][ny] = virus
                q.append((virus, s+1, nx, ny))

print(virus_map[target_x - 1][target_y - 1])

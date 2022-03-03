import copy
import collections
import sys

N = 0
M = 0
lab = [[0 for _ in range(8)] for _ in range(8)]  # 2차원 배열
mirror = [[0 for _ in range(8)] for _ in range(8)]  # 연구소의 복제본
q_virus_original = collections.deque()
answer = 0
num_clean = 0


def init_mirror():  # 연구소 복제본 초기화 과정
    global mirror  # 그냥 n m 복사하는 것.
    for r in range(N):
        for c in range(M):
            mirror[r][c] = lab[r][c]


def check_new_position(r, c, arr):  # 바이러스 갈수 있는 공간인지
    if r < 0 or r >= N or c < 0 or c >= M:
        return False
    if arr[r][c] != 0:
        return False
    return True


def do_virus():
    global answer
    q_virus = copy.deepcopy(q_virus_original)  # 바이러스 저장하는것을 복제해온다.
    lab_after_virus = copy.deepcopy(mirror)  # 바이러스가 다 퍼진 연구소 모습을 저장.
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    num_virus = 0
    while q_virus:  # 여기서 BFS 돌림
        r, c = q_virus.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            # 바이러스가 갈수 있는 범위 체크하는 함수
            if not check_new_position(nr, nc, lab_after_virus):
                continue
            lab_after_virus[nr][nc] = 2  # 바이러스 확산
            num_virus += 1
            q_virus.append((nr, nc))  # 새롭게 추가된 바이러스 좌표를 큐에 넣어 게속해서 BFS
    num_safe = num_clean - num_virus - 3  # 안전구역 체크 빈공간 - 신규바이러스 - 벽
    answer = max(answer, num_safe)


def build_wall(row, col, num_walls):
    if num_walls == 3:  # 종료조건 3개 다 지어졌을때
        do_virus()  # 바이러스 살포
        return
    col_begin = col
    for r in range(row, N):  # 00 부터 다 탐색하면 너무 느림 어디까지 갔는지 저장하고 그 이후 부터 탐색 = 입력 for문돌다가 조건에 맞으면 재귀함수를 통해서 벽을 세우는것이기때문 (r,c,num_wall)
        if r != row:  # 행의 값이 달라지면 0부터 같다면 바로 열부터 검색
            col_begin = 0
        for c in range(col_begin, M):
            if mirror[r][c] != 0:
                continue
            mirror[r][c] = 1
            build_wall(r, c, num_walls + 1)
            mirror[r][c] = 0


def solve():  # 큐에 저장했던 행렬정보로 정답을 구하기
    # 벽을 세울수 있는 모든 경우의 수 구하기
    for r in range(N):
        for c in range(M):
            if lab[r][c] != 0:  # 벽을 세울곳을 찾았으면 lab의 복제품 mirror에 적용하기
                continue
            init_mirror()  # 벽을 세울곳을 찾았으면 lab의 복제품 mirror에 적용하기
            mirror[r][c] = 1
            build_wall(r, c, 1)  # 벽을 한게 세웠으면 나머지 벽 2개를 세우기 위해 재귀 함수로 들어간다.
            mirror[r][c] = 0  # 재귀 함수가 끝나면 곧바로 1번째 벽을 부순다.
    print(answer)


N, M = map(int, sys.stdin.readline().split())
for r in range(N):
    # 한라인을 받아서 그 행의 각열에 접근해서 연구소를 나타내는 2차원 배열에 저장하는 방식
    l = list(map(int, sys.stdin.readline().split()))

    for c in range(M):  # 한줄 받고 각 원소들을 lab에 하나씩 저장함
        lab[r][c] = l[c]
        if lab[r][c] == 0:
            num_clean += 1   # 빈공간 갯수를 나중에 세기 그래서 입력받을때 받음.
        elif lab[r][c] == 2:
            q_virus_original.append((r, c))  # 바이러스 발견하면 큐에 바이러스 행렬 정보를 저장함.

solve()

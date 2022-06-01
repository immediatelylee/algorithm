# 10개 뭉치면 터짐 마지막

# 2차원 배열에서 배열내부의 요소들을 이동시킬수 있는지.

# bfs/dfs로 그룹을 찾고 , 그룹갯수를 반환하는 함수
# k가 넘었을때 삭제하는 함수,
# 이것들을 내려오게 하는 함수
# while으로 마지막까지 반복
def new_array(N):
    return [[False for i in range(10)] for _ in range(N)]


N, K = map(int, input().split())
M = [list(input()) for _ in range(N)]
ck = new_array(N)


def dfs(x, y):
    ck[x][y] = True  # 2 그룹에 있는가
    ret = 1  # 2
    for i in range(4):
        xx, yy = x+dx[i], y + dy[i]
        if xx < 0 or xx >= N or yy < 0 or yy >= 10:  # 구간 내에 있는지 체크
            continue
        if ck[xx][yy] or M[x][y] != M[xx][yy]:
            continue
        dfs(xx, yy)
        ret += dfs(xx, yy)  # 2
    return ret


def dfs2(x, y, val):
    ck2[x][y] = True  # 지워도 되는가
    for i in range(4):
        xx, yy = x+dx[i], y + dy[i]
    if xx < 0 or xx >= N or yy < 0 or yy >= 10:  # 구간 내에 있는지 체크
        continue
    if ck[xx][yy] or M[xx][yy] != val:
        continue


def down(x, y):  # 아래로 당기는 과정
    for i in range(10):
        tmp = []
        for j in range(N):
            if M[j][i] != 0:
                tmp.append(M[j][i])
        for j in range(N-len(tmp)):
            M[j][i] = 0
        for j in range(N-len(tmp)):
            M[j][i] = tmp[j-N+len(tmp)]


while True:  # 바뀌는게 있을떄 까지 반복
    exist = False
    for i in range(N):
        for j in range(10):
            if M[i][j] == 0 and not ck[i][j]:
                continue
            res = dfs(i, j)  # 갯수세기
            if res >= K:
                dfs2(i, j)  # 지우기
                exist = True
    if exist:
        break
    down()  # 내리기
for i in M:
    print(''.join(i))

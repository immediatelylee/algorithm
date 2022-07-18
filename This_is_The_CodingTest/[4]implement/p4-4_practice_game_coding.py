
# 북서남동 이동하기 (이동은 북서남동이지만 초기 방향은 북동남서임.) -> 헷갈리니까 북동남서로 지정하고 왼쪽 도는 함수를 만든다.
# 아직 가보지 않은 칸이 존재하면 가고 없다면 왼쪽 90도 만큼 회전
# 4방향 모두 이미 가본칸이거나 바다로 되어있는 칸인 경우에는 한칸 뒤로
import time

n, m = map(int, input().split())

# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
# 리스트 컴프리헨션
d = [[0] * m for _ in range(n)]

# 현재 캐릭터의 X좌표, Y좌표, 방향
x, y, direction = map(int, input().split())

# 전체 맵 정보 입력받기
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

start = time.time()


# 북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전


def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3


# 현재 좌표 방문 표시
d[x][y] = 1

# 시뮬레이션 시작
count = 1
turn_time = 0
while True:
    # 왼쪽으로 회전
    # d = turn_left(direction)?

    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue

    # 회전한 이후 정면에 가보지 않는 칸이 없거나 바다인 경우
    else:
        turn_time += 1

    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈 수 있다면 이동하기
        if array[nx][ny] == 0:
            x = nx
            y = ny

        # 뒤가 바다로 막혀있을 경우
        else:
            break

        turn_time = 0

print(count)


print(time.time()-start)

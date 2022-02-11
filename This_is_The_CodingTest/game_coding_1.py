n, m = map(int, input().split())
x, y, direction = input().split()
map_data = []
visited = [[0 for i in range(m)] for j in range(n)]


for j in range(m):
    map_data.append(list(input().split()))


# 회전을 어떻게 하지 시작 디렉션이 3일때  다 못도는 경우가 생김
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def turn90():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3


count = 1
turn_time = 0
while True:
    turn90()
    nx = x + dx[direction]
    ny = y + dy[direction]

    if visited[nx][ny] == 0 and map_data[nx][ny] == 0:
        visited[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        if map_data[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤가 바다인경우
        else:
            break
        turn_time = 0

print

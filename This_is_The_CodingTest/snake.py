n = int(input())  # 보드 크기
k = int(input())  # 사과 개수

snake_map = [[0]*(n+1) for _ in range(n+1)]
info = []

for i in range(k):
    x, y = map(int, input().split())
    snake_map[x][y] = 1

l = int(input())  # 방향변환 정보의 수
for i in range(l):
    x, c = input().split()
    info.append((int(x), y))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def turn(direction, c):
    if c == 'L':
        # direction-1 이 원본이였으나 음수를 나눌수도 있을것 같아 수정함.
        direction = (direction+3) % 4
    else:
        direction = (direction + 1) % 4
    return direction


def simulate():
    x, y = 1, 1
    snake_map[x][y] = 2
    direction = 0
    time = 0
    index = 0
    q = [(x, y)]
    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]

        if 1 <= nx and nx <= n and 1 <= ny and ny <= n and snake_map[nx][ny] != 2:
            # 사과가 없다면 이동 후에 꼬리 제거
            if snake_map[nx][ny] == 0:
                snake_map[nx][ny] = 2
                q.append((nx, ny))
                px, py = q.pop(0)
                snake_map[px][py] = 0
            # 사과가 있다면 이동 후에 꼬리 그대로 두기
            if snake_map[nx][ny] == 1:
                snake_map[nx][ny] = 2
                q.append((nx, ny))
        # 벽이나 뱀의 몸통과 부딪혔다면
        else:
            time += 1
            break
        x, y = nx, ny
        time += 1

        if index < l and time == info[index][0]:  # 회전할 시간인 경우 회전
            direction = turn(direction, info[index][1])
            index += 1
    return time


print(simulate())

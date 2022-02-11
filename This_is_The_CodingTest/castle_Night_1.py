input_data = input()
x = ord(input_data[0])-96
y = int(input_data[1])


# 마가 이동할수 있는 경우 벡터로
dx = [-1, 1, 2, 2, -1, 1, -2, -2]
dy = [2, 2, 1, -1, -2, -2, 1, -1]


# 탐색
cnt = 0
for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]
    # 맵밖으로 나가는 경우 제외
    if nx > 8 or ny > 8 or nx <= 0 or ny <= 0:
        continue
    cnt += 1

print(cnt)

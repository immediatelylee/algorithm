N = int(input())
move = list(input().split())  # 몰랐었는데 input().split() 로만 해도 자동으로 리스트 안에 넣어준다.

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

direction = ['L', 'R', 'U', 'D']
x, y = 1, 1

for i in move:
    for j in range(len(direction)):

        if move == direction[j]:
            nx = x + dx[j]
            ny = y + dy[j]

        if nx < 1 or ny < 1 or nx > N or ny > N:
            continue

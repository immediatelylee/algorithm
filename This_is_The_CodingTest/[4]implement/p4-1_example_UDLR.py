'''
1. nxn 공간에 1x1 정사각형으로 나눠져있음. 
2. 가장 왼쪽 위 좌표는 (1,1) , 가장 오른쪽 아래 좌표는 (N,N)
3. L 왼쪽한칸 ,R 오른쪽한칸, U 위로 한칸 , D 아래로 한칸 // 정사각형 공간을 넘어서는 움직임은 무시

ex) 
5
R R R U D D
-> 3 4
'''

n = int(input())
x, y = 1, 1

plans = input().split()

square_map = [[0 for _ in range(n)] for _ in range(n)]

directions = ['U', 'D', 'L', 'R']

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


for plan in plans:
    for i in range(len(directions)):
        if plan == directions[i]:
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 1 or ny < 1 or nx > n or ny > n:
                continue
            else:
                x = nx
                y = ny


print(x, y)

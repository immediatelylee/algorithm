import heapq
cnt = 1

INF = int(1e9)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def dijkstra():
    q = []
    heapq.heappush(q, (matrix[0][0], 0, 0))
    distance[0][0] = 0

    while q:
        cost, x, y = heapq.heappop(q)

        if x == matrix_size-1 and y == matrix_size - 1:
            print("Problem {0}: {1}".format(cnt, distance[x][y]))
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < matrix_size and 0 <= ny < matrix_size:
                nc = cost + matrix[nx][ny]

                if nc < distance[nx][ny]:
                    distance[nx][ny] = nc
                    heapq.heappush(q, (nc, nx, ny))


while 1:
    matrix_size = int(input())
    if matrix_size == 0:
        break

    matrix = []
    for _ in range(matrix_size):
        matrix.append(list(map(int, input().split())))

    distance = [[INF]*matrix_size for _ in range(matrix_size)]

    dijkstra()
    cnt += 1

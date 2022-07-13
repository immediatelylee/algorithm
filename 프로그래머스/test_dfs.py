from sys import stdin
n, m, v = map(int, stdin.readline().split())
matrix = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    line = list(map(int, stdin.readline().split()))
    matrix[line[0]][line[1]] = 1
    matrix[line[1]][line[0]] = 1

print(matrix)


def bfs(start):
    visited = [start]
    queue = [start]
    while queue:
        print("print:queue", queue)
        # pop 된 값이 n에 저장 pop quee에서는
        n = queue.pop(0)

        for c in range(len(matrix[start])):
            if matrix[n][c] == 1 and (c not in visited):
                print("print n:", n)
                print("print matrix:", matrix[n][c])
                visited.append(c)
                print("print visited:", visited)
                queue.append(c)

    return visited


# *는 변수의 개수를 알수 없을 때 사용한다.
# * args형태로 매개변수를 설정한다.
print(*bfs(v))

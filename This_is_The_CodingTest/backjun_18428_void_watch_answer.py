n = int(input())
school_map = []
for _ in range(n):
    school_map.append(list(input().split()))

height = len(school_map)
narrow = len(school_map[0])

direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
# dx = [1,-1,0,0]
# dy = [0,0,-1,1]


def bfs_seek(x, y):

    for i in range(4):
        tx, ty = direction[i]
        nx = x+tx
        ny = y+ty
        dfs_watch(nx, ny, i)


def dfs_watch(x, y, d):
    if x < 0 or y < 0 or x >= height or y >= narrow or school_map[x][y] == 'O':
        return
    if school_map[x][y] == 'S':
        return False

    if d == 0:
        nx = x - 1
        dfs_watch(nx, y, d)
    if d == 1:
        nx = x+1
        dfs_watch(nx, y, d)
    if d == 2:
        ny = y-1
        dfs_watch(x, ny, d)
    if d == 3:
        ny = y+1
        dfs_watch(x, ny, d)


for i in range(height):
    for j in range(narrow):
        pass

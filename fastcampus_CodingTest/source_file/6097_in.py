li = []
h, w = map(int, input().split())

for i in range(h):
    li.append([])
    for j in range(w):
        li[i].append(0)

n = int(input())
for i in range(n):
    l, d, x, y = map(int, input().split())
    for j in range(l):
        if d == 0:
            li[x-1][y-1] = 1
            y += 1
        else:
            li[x-1][y-1] = 1
            x += 1
for i in li:
    print(' '.join(map(str, i)))

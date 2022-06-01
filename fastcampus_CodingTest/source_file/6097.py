# d=[]
# for i in range(20) :
#     d.append([])
#     for j in range(20) :
#     d[i].append(0)

w, h = map(int, input().split())
n = int(input())

a = []
for i in range(h+1):
    a.append([])
    for j in range(w+1):
        a[i].append(0)

for i in range(n):
    l, d, x, y = map(int, input().split())
    if d == 0:
        for k in range(l):
            a[x][y + k] = 1
    else:
        for k in range(l):
            a[x+k][y] = 1

for i in range(1, h+1):
    for j in range(1, w+1):
        print(a[i][j], end=' ')
    print()

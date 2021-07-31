# https://www.acmicpc.net/problem/11650

location = []
for i in range(int(input())):
    x, y = input().split()
    location.append((int(x), int(y)))

result = sorted(location, key=lambda x: (x[0], x[1]))

for i in range(len(location)):
    print(result[i][0], result[i][1])

n, m = map(int, input().split())
map_point = []

for i in range(n):
    map_point.append(int(input()))


map_point.sort()
result = map_point[-1] // m

print(result)

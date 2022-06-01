n = int(input())
data = []

for _ in range(n):
    age, name = input().split()
    data.append((int(age), name))

result = sorted(data, key=lambda x: (x[0]))

for i in range(n):
    print(result[i][0], result[i][1], sep=' ')

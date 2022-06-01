n = int(input())

array = []
for i in range(n):
    input_data = input().split()
    array.append((int(input_data[0]), int(input_data[1])))

result = sorted(array)

for i in range(n):
    print(result[i][0], result[i][1], sep=' ')

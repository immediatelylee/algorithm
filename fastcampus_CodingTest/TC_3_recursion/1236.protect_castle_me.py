x, y = map(int, input().split())
array = []
for i in range(x):
    array.append(input())


row = [0]*x
column = [0]*y
row_count = 0
column_count = 0


for i in range(x):
    for j in range(y):
        if array[i][j] == 'X':
            row[i] = 1
            column[j] = 1


for i in range(x):
    if row[i] == 0:
        row_count += 1

for i in range(y):
    if column[i] == 0:
        column_count += 1

print(max(column_count, row_count))

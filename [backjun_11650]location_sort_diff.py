# https://www.acmicpc.net/problem/11650

import sys
n = int(sys.stdin.readline())

array = []
for i in range(n):
    input_data = sys.stdin.readline().split()
    array.append((int(input_data[0]), int(input_data[1])))

result = sorted(array)

for i in range(n):
    print(result[i][0], result[i][1], sep=' ')

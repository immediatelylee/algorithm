import sys
n, m = map(int, sys.stdin.readline().split())

array = []

for i in range(n):
    array.append(int(sys.stdin.readline()))

start = array[1]-array[0]
end = array[-1]-array[0]

'''
# Runtime error
n = int(input())
array = list(map(int, input().split()))
result = [0] * 100001
for i in range(n):
    result[array[i]] = 1

m = int(input())
data = list(map(int, input().split()))
for i in range(m):
    if result[data[i]] == 1:
        print(int(1))
    else:
        print(int(0))
'''
n = int(input())

data = set((map(int, input().split())))

m = int(input())
x = list(map(int, input().split()))

for i in x:
    if i not in data:
        print('0')
    else:
        print('1')

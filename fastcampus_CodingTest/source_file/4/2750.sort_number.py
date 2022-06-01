n = int(input())
array = []

for i in range(n):
    array.append(int(input()))

sc = sorted(array)

for i in range(n):
    print(sc[i], end='\n')

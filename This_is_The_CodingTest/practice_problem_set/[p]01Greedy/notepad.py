n = int(input())

data = list(map(int, input().split()))

data.sort()

cnt = 0
result = 0

for i in data:
    cnt += 1
    if cnt >= i:
        result += 1
        cnt = 0

n = int(input())
result = 0
count = 1

while n:
    if n >= count:
        n -= count
        count += 1
        result += 1
    else:
        count = 1

print(result)

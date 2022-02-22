n = list(map(int, input().split()))
result = 0
for i in range(len(n)):
    result += (n[i]*n[i])

print(result % 10)

n, m = map(int, input().split())
data = list(map(int, input().split()))
result = 0
sum_value = 0

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            sum_value = data[i] + data[j] + data[k]
            if sum_value <= m:
                result = max(sum_value, result)


print(result)

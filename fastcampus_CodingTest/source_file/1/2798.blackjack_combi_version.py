from itertools import combinations

n, m = map(int, input().split())
data = list(map(int, input().split()))
result = 0


combi = list(combinations(data, 3))


for i in combi:
    sum_combi = sum(i)
    if sum_combi <= m:
        result = max(result, sum_combi)

print(result)

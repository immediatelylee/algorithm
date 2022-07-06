N, M, K = map(int, input().split())


nums = list(map(int, input().split()))
nums.sort()
counts = 0
result = 0

for i in range(M):
    if counts != K:
        result += nums[-1]
        counts += 1
    else:
        result += nums[-2]
        counts = 0

print(result)

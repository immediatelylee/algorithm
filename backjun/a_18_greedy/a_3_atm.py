# https://www.acmicpc.net/problem/11399
n = int(input())
time = list(map(int, input().split()))


time.sort()
result = 0
presum = 0
for i in time:
    presum += i
    result += presum

print(result)

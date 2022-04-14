n = int(input())

date = []
reward = []
answer = [0]*(n+1)
max_value = 0

for i in range(n):
    x, y = map(int, input().split())
    date.append(x)
    reward.append(y)


for i in range(n-1, -1, -1):
    time = date[i] + i
    if time <= n:
        answer[i] = max(reward[i] + answer[time], max_value)
        max_value = answer[i]
    else:
        answer[i] = max_value

print(max_value)

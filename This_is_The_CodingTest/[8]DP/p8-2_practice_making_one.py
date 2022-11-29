'''
ai = min(ai-1,ai/2,ai/3,ai/5) +1
cnt 안돌리고 DP에 바텀업으로 접근한다.
나눠지는 경우를 찾아 memo[i] 와 memo[i // n] +1 을 최소값 비교를 한다. 
기존의 횟수와 나눠지는 경우 memop[몫] 의 경우에 계산이 한번더 들어간것 중 최소값을 찾아야 하기 때문
'''

x = int(input())
memo = [0] * 30001

for i in range(2, x+1):
    memo[i] = memo[i-1] + 1
    if i % 2 == 0:
        memo[i] = min(memo[i], memo[i // 2] + 1)
    if i % 3 == 0:
        memo[i] = min(memo[i], memo[i // 3] + 1)
    if i % 5 == 0:
        memo[i] = min(memo[i], memo[i // 5] + 1)

print(memo[x])

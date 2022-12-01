'''

ai = min(ai-1,ai/2,ai/3,ai/5) +1
    -   현재 수와 1차이 나는 경우
    -   현재 수가 2로 나누어 떨어지는 경우
    -   현재 수가 3로 나누어 떨어지는 경우
    -   현재 수가 5로 나누어 떨어지는 경우 
    -   모두 min함수로 비교한다. 

    -   각자의 경우를 각 if문으로 비교하여 비교할때마다 min으로 비교하고 dp에 저장한다.

cnt 안돌리고 DP에 바텀업으로 접근한다.
나눠지는 경우를 찾아 memo[i] 와 memo[i // n] +1 을 최소값 비교를 한다. 
기존의 횟수와 나눠지는 경우 memop[몫] 의 경우에 계산이 한번더 들어간것 중 
최소값을 찾아야 하기 때문
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

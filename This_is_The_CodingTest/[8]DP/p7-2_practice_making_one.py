'''
ai = min(ai-1,ai/2,ai/3,ai/5) +1
cnt 안돌리고 dp에 바텀업으로 접근한다.
나눠지는 경우를 찾아 d[i] 와 d[i // n] +1 을 최소값 비교를 한다. 
기존의 횟수와 나눠지는 경우 dp[몫] 의 경우에 계산이 한번더 들어간것 중 최소값을 찾아야 하기 때문
'''

x = int(input())
d = [0] * 30001

for i in range(2, x+1):
    d[i] = d[i-1] + 1
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
    if i % 5 == 0:
        d[i] = min(d[i], d[i // 5] + 1)

print(d[x])

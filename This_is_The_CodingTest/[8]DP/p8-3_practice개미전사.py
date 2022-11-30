'''
dp 0,1 을 지정해준다.
ai = max(ai-1,ai-2+k)
'''

n = int(input())
dp = [0]*100
b_store = list(map(int, input().split()))

dp[0] = b_store[0]
dp[1] = max(b_store[0], b_store[1])

for i in range(2, len(b_store)):
    dp[i] = max(dp[i-1], dp[i-2]+b_store[i])

print(dp[n-1])

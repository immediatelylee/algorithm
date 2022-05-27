# https://www.acmicpc.net/problem/2798
# 배열 완전탐색

N, M = map(int, input().split())
Cards = list(map(int, input().split()))
answer = 0

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            result = Cards[i]+Cards[j]+Cards[k]

            if result <= M and answer <= result:

                answer = result


print(answer)

# 3중for문돌려도 n의 범위가 3<= n <= 100  이므로  n^3은 100만 시간제한이 1초이므로
# 초당 2000만 계산을 하는 파이썬에서는 거뜬히 돌아간다.

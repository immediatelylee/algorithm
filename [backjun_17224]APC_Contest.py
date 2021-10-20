# https://www.acmicpc.net/problem/17224
N, L, K = map(int, input().split())  # 문제갯수,역량,최대갯수
easy, hard = 0, 0
for i in range(N):
    x, y = map(int, input().split())  # x 쉬운문제,y 어려운문제
    if y <= L:
        hard += 1
    elif x <= L:
        easy += 1
if hard >= K:
    print(K*140)
elif K > hard and (hard+easy) >= K:
    print(hard*140 + (K-hard)*100)
elif (hard+easy) < K:
    print(easy*100)

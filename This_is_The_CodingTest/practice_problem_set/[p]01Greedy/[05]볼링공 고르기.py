import sys

n, m = map(int, input().split())
ball_weight = list(map(int, input().split()))
# 1부터 10까지의 무게를 담을 수 있는 리스트
weight_list = [0]*(m+1)

for weight in ball_weight:
    # 각 무게에 해당하는 볼링공의 개수 카운트
    weight_list[weight] += 1

cnt = 0
# 1부터 m까지의 각 무게에 대하여 처리
for i in range(1, m+1):
    n -= weight_list[i]  # 무게가 i인 볼링공의 개수(A가 선택할 수 있는 개수) 제외
    cnt += weight_list[i] * n  # B가 선택하는경우의수 곱하기

print(cnt)

# 5 3
# 1 3 2 3 2 -> 8

# 8 5
# 1 5 4 3 2 4 5 2 -> 25

# 1 :1  2:2 3:2 라고 가정
# 1(무게가 1인 개수) *4(B가 선택하는 개수)
# 2(무게가 2인 개수) * 2(B가 선택하는 개수)
# 2(무게가 3인 개수) *0(B가 선택하는 개수)
# 총 8가지

# n은 볼링공의 개수, m은 공의 최대무게
n, m = map(int, input().split())
ball = map(int, input().split())

weight = [0]*11
for x in ball:
    weight[x] += 1

result = 0

for i in range(1, m+1):
    n -= weight[i]  # 무게가 i인 볼링공의 개수 (A가 선택할 수 있는 개수) 제외
    result += weight[i]*n  # B가 선택하는 경우의 수와 곱하기
print(result)

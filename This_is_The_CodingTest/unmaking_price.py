
# 1 ~ target-1까지 모든 금액을 만들수 있는 상태


# 1부터 target-1까지 모든 금액을 만들수 있는 상태라면 현재 확인하는 동전을 통해 target을 만들수 있는지
#  ###현재 확인하는 동전의 단위가 target이하인지  ###
# 1 3 5  -> 2를 구할수 없음


n = int(input())
data = list(map(int, input().split()))
data.sort()

target = 1
for x in data:
    if target < x:
        break
    target += x

print(target)

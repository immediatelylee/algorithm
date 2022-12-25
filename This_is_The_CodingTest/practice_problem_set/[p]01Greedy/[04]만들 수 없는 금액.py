n = int(input())
coin_type = list(map(int(input().split())))
coin_type.sort()

target = 1
for x in coin_type:
    # 만들 수 없는 금액을 찾았을 때 반복 종료
    if target < x:
        break
    target += x

# 만들 수 없는 금액 출력
print(target)

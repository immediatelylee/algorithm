# 현재 그룹에 포함된 모험가의 수가  현재 확인하고 있는 공포도 보다 크다면 그룹으로 설정한다.
n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0
count = 0

for i in data:
    count += 1
    if count >= i:
        result += 1
        count = 0

print(result)

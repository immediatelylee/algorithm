n = int(input())
gild = list(map(int, input().split()))
gild.sort()

result = 0
count = 0

for i in gild:  # 공포도 낮은 순으로 하나씩 확인하며
    count += 1  # 현재 그룹에 해당 모험가를 포함시키기
    if count >= i:  # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
        result += 1  # 총 그룹의 수 증가시키기
        count = 0  # 현재 그룹에 포함된 모험가의 수 초기화

print(result)  # 총 그룹의 수 출력

# 4/5 답안 수정함
# 테스트 case 추가로 기존의 답변들이 80%에서 오답처리되었음
# 최소를 array[1] - array[0] -> 1 로 변경함.
import sys
input = sys.stdin.readline
n, c = list(map(int, input().split(' ')))
array = []

for _ in range(n):
    array.append(int(input()))
array = sorted(array)

start = 1
end = array[-1] - array[0]
result = 0

while(start <= end):
    mid = (start + end) // 2  # mid는 Gap을 의미합니다.
    value = array[0]
    count = 1
    for i in range(1, len(array)):
        if array[i] >= value + mid:
            value = array[i]
            count += 1
    if count >= c:  # c개 이상의 공유기를 설치할 수 있는 경우
        start = mid + 1
        result = mid
    else:  # c개 이상의 공유기를 설치할 수 없는 경우
        end = mid - 1

print(result)

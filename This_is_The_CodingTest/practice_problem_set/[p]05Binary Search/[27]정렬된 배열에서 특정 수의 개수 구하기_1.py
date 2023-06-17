import bisect

# 입력
n, x = map(int, input().split())
data = list(map(int, input().split()))

# bisect 함수를 이용하여 값이 x인 원소의 개수 계산
count = bisect.bisect_right(data, x) - bisect.bisect_left(data, x)

# 값이 x인 원소가 하나도 없는 경우 -1 출력
if count == 0:
    print(-1)
else:
    print(count)

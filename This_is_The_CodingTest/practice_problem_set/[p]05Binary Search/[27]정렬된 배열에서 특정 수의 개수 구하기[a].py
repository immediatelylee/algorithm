import bisect

n, x = map(int, input().split())
array = list(map(int, input().split()))

# bisect_left(a, x): 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 왼쪽 인덱스를 반환
left = bisect.bisect_left(array, x)

# bisect_right(a, x): 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 오른쪽 인덱스를 반환
right = bisect.bisect_right(array, x)

if right - left == 0:
    print(-1)
else:
    print(right - left)


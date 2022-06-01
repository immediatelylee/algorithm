n = int(input())
array = []
for _ in range(n):
    x, y = map(int, input().split())
    array.append((x, y))

# 파이썬의 기본 정렬 라이브러리는 기본적으로 튜블의 인덱스 순서대로 오름차순 정렬 한다.
# x좌표가 같다고 한다면 y좌표를 정렬하는 것은 파이썬의 기본 정렬 라이브러리이다.
array = sorted(array)

for i in array:
    print(i[0], i[1])

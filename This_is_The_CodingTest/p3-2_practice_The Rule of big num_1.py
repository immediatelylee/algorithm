# N, M, K를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())

# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort()
first = data[n - 1]  # 가장 큰 수를
second = data[n - 2]  # 두번째로 큰 수를

result = 0

while True:
    for i in range(k):  # 가장 큰 수 k번 더하기
        if m == 0:
            break
        result += first
        m -= 1  # 더할 때마다 1씩 빼기

    if m == 0:
        break
    result += second  # 두번째로 큰 수 한 번 더하기
    m -= 1  # 더할 때마다 1빼기

print(result)

def find(x):
    if x == parent[x]:
        return x
    else:
        p = find(parent[x])
        parent[x] = p
        return parent[x]


def union(x, y):
    x = find(x)
    y = find(y)

    if x != y:
        parent[y] = x
        number[x] += number[y]


test_case = int(input())

for i in range(test_case):
    # 입력 값이 문자열이기 때문에 리스트로 만드는 것은 어렵다.
    parent = dict()
    number = dict()

    f = int(input())

    for _ in range(f):
        # 입력값 받기
        x, y = input().split()

        if x not in parent:
            parent[x] = x
            number[x] = 1

        if y not in parent:
            parent[y] = y
            number[y] = 1

    union(x, y)
    print(number[find(x)])

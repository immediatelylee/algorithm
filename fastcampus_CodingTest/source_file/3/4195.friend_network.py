parent = []
test_case = int(input())
n = int(input())

# union - find 알고리즘은 합집합 찾기다!
# 어떤 기준으로 묶느냐? 공통된 부모를 통하여 묶는다.
# 묶을때 재귀적 방법을 통한 반복을 통하여 구한다.


def find(x):
    if x == parent[x]:
        return x
    else:
        # 재귀적으로 실제 부모를 찾는다.
        p = find(parent[x])
        parent[x] = p
        return parent[x]

# union !  부모를 같게 묶어준다.


def union(x, y):
    x = find(x)
    y = find(y)

    if x != y:
        parent[y] = x
        number[x] += number[y]


for i in range(test_case):
    parent = dict()
    number = dict()

    f = int(input())

    for _ in range(f):
        x, y = input().split()

        if x not in parent:
            parent[x] = x
            number[x] = 1

        if y not in parent:
            parent[y] = y
            number[y] = 1
    union(x, y)
    print(number[find(x)])

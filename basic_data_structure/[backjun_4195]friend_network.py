# https://www.acmicpc.net/problem/4195

# 1. make - set
# 2. find
# 3. union


# 재귀적으로 부모를 찾아서 자신의 부모로 삼음
def find(x):
    if x == parent[x]:
        return x
    else:
        p = find(x)
        parent[x] = p
        return p


def union(x, y):
    x = find(x)
    y = find(y)

    if x != y:
        parent[y] = x
        number[x] += number[y]


for testcase in range(int(input())):
    parent = dict()
    number = dict()

    for _ in range(int(input())):
        x, y = input().split()

        # make-set
        if x not in parent:
            parent[x] = x
            number[x] = 1
        if y not in parent:
            parent[y] = y
            number[y] = 1

        union(x, y)
        print(number[find(x)])

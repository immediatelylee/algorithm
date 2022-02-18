# Union-find
# 서로소 집합 , union함수와 find함수로 구분
# 1. 입력을 받고 각각의 부모노드를 위한 리스트도 만든다.
# 2.

#


n, m = map(int, input().split())


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

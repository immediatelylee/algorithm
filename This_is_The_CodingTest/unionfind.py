# Union-find
# 서로소 집합 , union함수와 find함수로 구분
# 1. 입력을 받고 각각의 부모노드를 위한 리스트도 만든다.
# 2.

#


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]  # 압축방식


def union_parent(parent, a, b):  # find함수를 이용
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


v, e = map(int, input().split())

parent = [0] * (v+1)   # 부모리스트 생성(위에 압축으로 루트노드가 저장됨.)

for i in range(1, v+1):  # 각자의 노드부모를 각자 로 설정
    parent[i] = i

for i in range(e):
    a, b, = map(int, input().split())

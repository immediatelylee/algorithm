# Union-find
# 서로소 집합 , union함수와 find함수로 구분
# 1. 입력을 받고 각각의 부모노드를 위한 리스트도 만든다.
# 2. find_parent는 자신과 parent가 같지 않으면 같을때 까지 재귀함수로 find를 한다.
# 3. union_parent는 find함수를 이용해서 a,b를 선언하고 부모 노드가 큰쪽이 작은쪽의 부모 노드룰  선언한다.  작은노드가 부모
# 4. 각자노드의 부모를 각자노드로 설정하고
# 5. for문을 통하여 union함수를 실행한다.

# 입력값
'''
6 4
1 4
2 3
2 4
5 6
'''


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
    a, b = map(int, input().split())
    union_parent(parent, a, b)

print('각 원소가 속한집합: ')
for i in range(1, v+1):
    print(find_parent(parent, i), end=' ')

print()

print('부모테이블')
for i in range(1, v+1):
    print(parent[i], end=' ')

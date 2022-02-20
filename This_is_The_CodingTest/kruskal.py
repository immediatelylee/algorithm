# 신장트리는 루프를 돌지않는 트리이면서 모든 노드를 포함하는 부분그래프를 말한다.
# 여기에 최소 비용을 가지는 신장트리를 최소신장트리라고 한다.

# 간선의 데이터를 비용에 다라 오름차순으로 정렬한다.
# 간선을 하나씩 확인하며 현재의 간선이 사이클을 발생시키는지 확인한다.
# 사이클이 도는지 확인하려면 모든 루트 노드가 같다면 사이클이 도는 것이다.
# 모든 간선에 대해 사이클을 발생하는지 확인한다.

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


v, e = map(int, input().split())

parent = [0] * (v+1)

edges = []
result = 0

for i in range(1, v+1):
    parent[i] = i

for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()

for edge in edges:
    cost, a, b = edge

    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)

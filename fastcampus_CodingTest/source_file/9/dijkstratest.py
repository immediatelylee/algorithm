import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n+1)]
print(graph)
distance = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

print(graph)
# def dijkstra(start):
#     q = []
#     heapq.heappush(q,(0,start))
#     distance[start]= 0
#     while q:
#         dist,now = heapq.heappop(q)
#         if distance[now]

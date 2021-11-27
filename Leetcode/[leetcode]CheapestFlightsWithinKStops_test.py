# https://leetcode.com/problems/cheapest-flights-within-k-stops/

import collections
import heapq
import sys
from typing import List

n = 3
flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
src = 0
dst = 2
K = 1


def findCheapestPrice(n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
    graph = collections.defaultdict(list)
    weight = [(sys.maxsize, K)] * n
    # 그래프 인접 리스트 구성
    for u, v, w in flights:
        graph[u].append((v, w))

    # 큐 변수: [(가격, 정점, 남은 가능 경유지 수)]
    Q = [(0, src, K)]

    # 우선 순위 큐 최소값 기준으로 도착점까지 최소 비용 판별
    while Q:
        price, node, k = heapq.heappop(Q)
        if node == dst:
            return price
        if k >= 0:
            for v, w in graph[node]:
                alt = price + w
                if alt < weight[v][0] or k-1 >= weight[v][1]:
                    weight[v] = (alt, k-1)
                    heapq.heappush(Q, (alt, v, k - 1))
    return -1


print(findCheapestPrice(n, flights, src, dst, K))
# TLM
# def findCheapestPrice(n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
#     graph = collections.defaultdict(list)
#     # 그래프 인접 리스트 구성
#     for u, v, w in flights:
#         graph[u].append((v, w))

#     # 큐 변수: [(가격, 정점, 남은 가능 경유지 수)]
#     Q = [(0, src, K)]

#     # 우선 순위 큐 최소값 기준으로 도착점까지 최소 비용 판별
#     while Q:
#         price, node, k = heapq.heappop(Q)
#         if node == dst:
#             return price
#         if k >= 0:
#             for v, w in graph[node]:
#                 alt = price + w
#                 heapq.heappush(Q, (alt, v, k - 1))
#     return -1

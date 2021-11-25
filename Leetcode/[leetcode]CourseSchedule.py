import collections
from typing import List


# class Solution:
#     def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
#         graph = collections.defaultdict(list)
#         # 그래프 구성
#         for x, y in prerequisites:
#             graph[x].append(y)

#         traced = set()

#         def dfs(i):
#             # 순환 구조이면 False
#             if i in traced:
#                 return False

#             traced.add(i)
#             for y in graph[i]:
#                 if not dfs(y):
#                     return False
#             # 탐색 종료 후 순환 노드 삭제
#             traced.remove(i)

#             return True

#         # 순환 구조 판별
#         for x in list(graph):
#             if not dfs(x):
#                 return False

#         return True

numCourses = 2
# prerequisites = [[1, 0]]
# prerequisites = [[1, 0], [0, 1]]
prerequisites = [[1, 0], [2, 1], [3, 2], [5, 1]]


def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    graph = collections.defaultdict(list)
    # 그래프 구성
    for x, y in prerequisites:
        graph[x].append(y)

    traced = set()

    def dfs(i):
        # 순환 구조이면 False
        if i in traced:
            return False

        traced.add(i)
        for y in graph[i]:
            if not dfs(y):
                return False
        # 탐색 종료 후 순환 노드 삭제
        traced.remove(i)

        return True

    # 순환 구조 판별
    for x in list(graph):
        if not dfs(x):
            return False

    return True


print(canFinish(numCourses, prerequisites))

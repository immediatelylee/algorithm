from typing import List
import itertools

# n = 4
# k = 2


class Solution:
    def combi(self, n: int, k: int) -> List[List[int]]:

        return list(map(list, itertools.combinations(range(1, n+1), k)))


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return list(map(list, itertools.combinations(range(1, n + 1), k)))
# test 코드
# test = Solution()
# print(test.combi(n, k))

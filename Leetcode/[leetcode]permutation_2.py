# from itertools import permutations
# from typing import List

from typing import List
import itertools
nums = [1, 2, 3]

# result = []

# # 튜플로 나오는 결과를 [[]] 로 저장하려면?  -> map 이용
# # permutations(nums,r)에서 r은 생략가능함


# def permulation(nums: List) -> List[List]:
#     return list(map(list, permulation(nums)))


# permulation(nums)


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(map(list, itertools.permutations(nums)))


# test 코드
test = Solution()
print(test.permute(nums))

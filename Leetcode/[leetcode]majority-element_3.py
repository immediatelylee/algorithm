# https://leetcode.com/problems/majority-element
from typing import List
import collections
nums = [2, 2, 1, 1, 1, 2, 2]


class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        if not nums:
            return None
        if len(nums) == 1:
            return nums[0]

        half = len(nums) // 2
        a = self.majorityElement(nums[:half])
        b = self.majorityElement(nums[half:])

        return [b, a][nums.count(a) > half]


test = Solution()
print(test.majorityElement(nums))

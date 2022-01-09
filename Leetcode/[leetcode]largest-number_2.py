
from functools import cmp_to_key

from typing import List

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        nums = sorted(map(str, nums), key = cmp_to_key(lambda x, y : int(y + x) - int(x + y)))
        
        return ''.join(nums) if nums[0] != '0' else '0'

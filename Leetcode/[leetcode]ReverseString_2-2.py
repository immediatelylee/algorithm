# https://leetcode.com/problems/reverse-string/
from typing import List
s = ["h", "e", "l", "l", "o"]


class Solution:
    def reverseString(self, s: List[str]) -> None:
        # 공간복잡도가 (1) 이여야하므로 
        s[:] = s[::-1]

        return s


test = Solution()
print(test.reverseString(s))

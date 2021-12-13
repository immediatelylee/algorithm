# https://leetcode.com/problems/reverse-string/
from typing import List
s = ["h", "e", "l", "l", "o"]


class Solution:
    def reverseString(self, s: List[str]) -> None:

        left, right = 0, len(s)-1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return s


test = Solution()
print(test.reverseString(s))

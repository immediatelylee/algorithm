# https://leetcode.com/problems/reverse-string/
from typing import List
s = ["h", "e", "l", "l", "o"]


class Solution:
    def reverseString(self, s: List[str]) -> None:

        word = s[::-1]

        return word


test = Solution()
print(test.reverseString(s))

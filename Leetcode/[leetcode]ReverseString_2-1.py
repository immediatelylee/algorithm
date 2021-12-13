# https://leetcode.com/problems/reverse-string/
from typing import List
s = ["h", "e", "l", "l", "o"]


class Solution:
    def reverseString(self, s: List[str]) -> None:

        s.reverse()

        return s

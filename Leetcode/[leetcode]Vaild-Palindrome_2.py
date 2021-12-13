# https://leetcode.com/problems/valid-palindrome/
from collections import deque
s = "A man, a plan, a canal: Panama"


class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = deque()
        for i in s:
            if i.isalnum():
                strs.append(i.lower())

        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False

        return True


test = Solution()
print(test.isPalindrome(s))

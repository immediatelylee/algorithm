# https://leetcode.com/problems/valid-palindrome/
import re

s = "A man, a plan, a canal: Panama"


class Solution:
    def isPalindrome(self, s: str) -> bool:

        s.lower()
        s = re.sub('[^a-z0-9]', '', s)
        return s == s[::]


test = Solution()
print(test.isPalindrome(s))

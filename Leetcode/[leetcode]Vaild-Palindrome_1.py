# https://leetcode.com/problems/valid-palindrome/

s = "A man, a plan, a canal: Panama"
# 1. use list


class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = []
        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        # Check palindrome
        while len(strs) > 1:
            if strs.pop(0) != strs.pop():
                return False

        return True


test = Solution()
print(test.isPalindrome(s))

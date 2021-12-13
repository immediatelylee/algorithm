# https://leetcode.com/problems/valid-palindrome/
s = "A man, a plan, a canal: Panama"


class Solution:
    def isPalindrome(self, s: str) -> bool:
        input_data = []
        s.lower()
        for i in s:
            if i.isalnum():
                input_data.append(i)

        return input_data == input_data[::]


test = Solution()
print(test.isPalindrome(s))

# https://leetcode.com/problems/reverse-string/

# s = list("hello")
s = ["H", "a", "n", "n", "a", "h"]

# 1  two pointer
left, right = 0, len(s)-1
while left < right:
    s[left], s[right] = s[right], s[left]
    left += 1
    right -= 1

# class Solution:
#     def reverseString(self, s: List[str]) -> None:

#         left,right =0,len(s)-1
#         while left < right:
#             s[left],s[right] =s[right],s[left]
#             left += 1
#             right -= 1
#         """
#         Do not return anything, modify s in-place instead.
#         """


# 2 reverse()

s = ["H", "a", "n", "n", "a", "h"]

s.reverse()

# class Solution:
#     def reverseString(self, s: List[str]) -> None:

#         s[:] = s[::-1]
#         """
#         Do not return anything, modify s in-place instead.
#         """


# 3 slice list

s[:] = s[::-1]

# class Solution:
#     def reverseString(self, s: List[str]) -> None:

#         s.reverse()
#         """
#         Do not return anything, modify s in-place instead.
#         """

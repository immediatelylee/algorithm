# https://leetcode.com/problems/remove-duplicate-letters/

# 미완성  왜 ! return을 안하냐고!
# print(removeDuplicateLetters(s)) 이런식으로 출력해야함.
s = 'cbacdcbc'


def removeDuplicateLetters(s: str) -> str:
    # 집합으로 정렬
    for char in sorted(set(s)):
        suffix = s[s.index(char):]
        # 전체 집합과 접미사 집합이 일치할때 분리 진행
        if set(s) == set(suffix):
            return char + removeDuplicateLetters(suffix.replace(char, ''))
    return ''


print(removeDuplicateLetters(s))


# class Solution:
#     def removeDuplicateLetters(self, s: str) -> str:
#         # 집합으로 정렬
#         for char in sorted(set(s)):
#             suffix = s[s.index(char):]
#             # 전체 집합과 접미사 집합이 일치할때 분리 진행
#             if set(s) == set(suffix):
#                 return char + self.removeDuplicateLetters(suffix.replace(char, ''))
#         return ''

# https://leetcode.com/problems/minimum-window-substring/
# time out - bruteforce

from typing import List

s = "ADOBECODEBANC"
t = "ABC"


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def contains(s_substr_lst: List, t_lst: List):
            # 슬라이딩 윈도우 내에 있으면 제거 후, True 리턴
            for t_elem in t_lst:
                if t_elem in s_substr_lst:
                    s_substr_lst.remove(t_elem)
                else:
                    return False
            return True

        if not s or not t:
            return ''

        window_size = len(t)

        # range는 그 전 범위까지만 찾으므로 + 1
        # 여기서는 window_size가 t를 시작으로 한칸씩 증가 (최대 s의 길이)
        for size in range(window_size, len(s) + 1):
            for left in range(len(s) - size + 1):
                s_substr = s[left:left + size]

                if contains(list(s_substr), list(t)):
                    return s_substr
        return ''

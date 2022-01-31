# https://leetcode.com/problems/binary-search/
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(left, right):
            if left <= right:
                mid = (left + right) // 2
                # 버그 개선은 다음과 같이 (자료형 최댓값)
                # mid = left + (right - left) // 2

                if nums[mid] < target:
                    return binary_search(mid + 1, right)
                elif nums[mid] > target:
                    return binary_search(left, mid - 1)
                else:
                    return mid

            else:
                return -1

        return binary_search(0, len(nums) - 1)

# https://leetcode.com/problems/permutations/

from typing import List
nums = [1, 2, 3]


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        prev_elements = []

        def dfs(elements):
            # 리프 노드일때 결과 추가
            if len(elements) == 0:
                results.append(prev_elements[:])

            # 순열 생성 재귀 호출
            for e in elements:
                next_elements = elements[:]
                next_elements.remove(e)

                prev_elements.append(e)
                dfs(next_elements)
                prev_elements.pop()

        dfs(nums)
        return results


# test Code

test = Solution()
print(test.permute(nums))


'''
원소별로 탐색 
1 2 3  1 3 2
2 1 3  2 3 1
3 1 2  3 2 1

A (0:3)                             [ ]

A (1:3)             [1]             [2]             [3]

A (2:3)      [1,2] [1,3]        [2,1] [2,3]      [3,1] [3,2]

A (3:3) [1,2,3] [1,3,2]      [2,1,3] [2,3,1]    [3,1,2] [3,2,1]
'''

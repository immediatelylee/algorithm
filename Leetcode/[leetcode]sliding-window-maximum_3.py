
from collections import deque
from typing import List


class Solution:

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = deque([])
        for i in range(k):
            # 이전 숫자가 현재 숫자보다 작다는 것을 발견하면 pop ②
            while l and nums[i] >= nums[l[-1]]:
                l.pop()

            # 순서대로 deque에 넣어준다 ①
            l.append(i)
        # 가장 큰 값은 우선순위 큐에서 첫번째 값
        ans = [nums[l[0]]]

        # window에서 첫 번째 숫자가 가장 크고 두 번째 숫자가 두 번째로 큰지 확인합니다
        for i in range(1, len(nums)-k+1):

            while(l and nums[i+k-1] >= nums[l[-1]]):
                l.pop()

            l.append(i+k-1)

            # window가 지나면 가장 큰 것을 pop
            if i-1 == l[0]:
                l.popleft()
            ans.append(nums[l[0]])
        return ans

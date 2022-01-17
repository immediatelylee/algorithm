# https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)

        # 정렬된 딕셔너리 (원래 해시테이블은 입력순서가 유지되지 않는다)
        dp = collections.OrderedDict()
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])

        for i in range(2, len(nums)):
            # 두번째 값이라고 한다면 그 첫번째 값과 세번째 값이 더해지는 것
            # 한 칸 이상 떨어진 집만 훔칠 수 있기 때문
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp.popitem()[1]

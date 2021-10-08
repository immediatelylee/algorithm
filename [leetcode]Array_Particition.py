# https://leetcode.com/problems/array-partition-i/

# 1. sort
nums = [1, 4, 3, 2]
result = 0

nums.sort()
pair = []

for i in nums:
    pair.append(i)
    if len(pair) == 2:
        result += min(pair)
        pair = []

print(result)

# from typing import List


# class Solution:
#     def arrayPairSum(self, nums: List[int]) -> int:
#         sum = 0
#         pair = []
#         nums.sort()

#         for n in nums:
#             # 앞에서 부터 오름차순으로 페어를 만들어 합 계산
#             pair.append(n)
#             if len(pair) == 2:
#                 sum += min(pair)
#                 pair = []

#         return sum

# 2. even

# from typing import List


# class Solution:
#     def arrayPairSum(self, nums: List[int]) -> int:
#         sum = 0
#         nums.sort()

#         for i, n in enumerate(nums):
#             # 짝수 번째 값의 합 계산
#             if i % 2 == 0:
#                 sum += n

#         return sum


# 3. python
# from typing import List


# class Solution:
#     def arrayPairSum(self, nums: List[int]) -> int:
#         return sum(sorted(nums)[::2])

# https://leetcode.com/problems/two-sum/
# 두수의합

# 1  bruteforce
# nums = [2,7,11,15]
# target = 9

# for i in range(len(nums)):
#     for j in range(i+1,len(nums)):
#         if nums[i] + nums[j] == target:
#             print([i,j])


# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i,j]


# 2   in 활용
# nums = [2,7,11,15]
# target =9

# for i, n in enumerate(nums):
#     complement = target -n

#     if complement in nums[i+1:]:
#         print(nums.index(n),nums[i+1:].index(complement) +(i+1))


# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i, n in enumerate(nums):
#             complement = target -n

#             if complement in nums[i+1:]:
#                 return nums.index(n),nums[i+1:].index(complement) +(i+1)

# 3 첫번째 수를 뺀 결과 키 조회

nums = [2,7,11,15]
target =9
nums_map={}
# 키와 값을 바꿔서 딕셔너리로 저장
for i,num in enumerate(nums):
    nums_map[num]=i

# 타겟에서 첫 번째 수를 뺀 결과를 키로 조회
for i,num in enumerate(nums):
    if target -num in nums_map and i != nums_map[target - num]:
        print(nums.index(num) , nums_map[target -num])

        # return nums.index(num) , nums_map[target -num]
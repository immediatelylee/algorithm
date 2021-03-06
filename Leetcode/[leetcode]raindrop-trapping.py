# 1 two point
# from typing import List

# height = [2, 1, 3, 0, 1, 2]
# # height = [4, 2, 0, 3, 2, 5]
# if not height:
#     print(0)

# volume = 0
# left, right = 0, len(height) - 1
# left_max, right_max = height[left], height[right]

# while left < right:
#     left_max, right_max = max(height[left], left_max), max(
#         height[right], right_max)
#     # 더 높은 쪽을 향해 투 포인터 이동
#     if left_max <= right_max:
#         volume += left_max - height[left]
#         left += 1
#     else:
#         volume += right_max - height[right]
#         right -= 1
# print(volume)


# class Solution:
#     def trap(self, height: List[int]) -> int:
#         if not height:
#             return 0

#         volume = 0
#         left, right = 0, len(height) - 1
#         left_max, right_max = height[left], height[right]

#         while left < right:
#             left_max, right_max = max(height[left], left_max), max(
#                 height[right], right_max)
#             # 더 높은 쪽을 향해 투 포인터 이동
#             if left_max <= right_max:
#                 volume += left_max - height[left]
#                 left += 1
#             else:
#                 volume += right_max - height[right]
#                 right -= 1
#         return volume


# 2 stack

from typing import List
# height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
height = [4, 2, 0, 3, 2, 5]

stack = []
volume = 0

for i in range(len(height)):
    # 변곡점을 만나는 경우
    while stack and height[i] > height[stack[-1]]:
        # 스택에서 꺼낸다
        top = stack.pop()

        if not len(stack):
            break

        # 이전과의 차이만큼 물 높이 처리
        distance = i - stack[-1] - 1
        waters = min(height[i], height[stack[-1]]) - height[top]

        volume += distance * waters

    stack.append(i)
print(volume)


# from typing import List

# class Solution:
#     def trap(self, height: List[int]) -> int:

#         stack = []
#         volume = 0

#         for i in range(len(height)):
#             # 변곡점을 만나는 경우
#             while stack and height[i] > height[stack[-1]]:
#                 # 스택에서 꺼낸다
#                 top = stack.pop()

#                 if not len(stack):
#                     break

#                 # 이전과의 차이만큼 물 높이 처리
#                 distance = i - stack[-1] - 1
#                 waters = min(height[i], height[stack[-1]]) - height[top]

#                 volume += distance * waters

#             stack.append(i)
#         return volume

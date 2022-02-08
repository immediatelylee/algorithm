# https://leetcode.com/problems/reverse-linked-list-ii/


from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def add(val):
        ListNode = head
        while ListNode.next:
            ListNode = ListNode.next
        ListNode.next = ListNode(val)


# case1
head = [1, 2, 3, 4, 5]
left = 2
right = 4

# case2
# head = [5]
# left = 1
# right = 1

# class Solution:
#     def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
#         array = []
#         for i in range(len(head)):
#             array.append(head[i])

#         reverse_array = array[left:right].reverse()
#         print(reverse_array)

# reverse를 어떻게 효과적으로 하지?


array = []
array2 = []
reverse_array = []
for i in range(len(head)):
    if i >= left-1 and i <= right-1:
        reverse_array.append(head[i])
    elif i < left - 1:
        array.append(head[i])
    else:
        array2.append(head[i])

for i in reversed(reverse_array):
    array.append(i)
for i in array2:
    array.append(i)


# list2node
result_node = ListNode()

for i, num in enumerate(array):
    if i == 0:
        result_node.val = num
    else:
        node = result_node
        while node.next != None:
            node = node.next
        node.next = ListNode(num)

print(list(ListNode))
# ImportError: cannot import name 'ListNode' from 'typing' 이 에러 뭐지
# 없어서 나는것 class ListNode를 따로 만들어야 하는것이다 import하는 것이 아니라

# 연결리스트를 어떻게 보지?


# for i in range(len(head)):
#     array.append(head[i])


# reverse_array = list(reversed(array[left-1:right]))
# print(reverse_array)


# test = Solution()
# print(test.reverseBetween(head, left, right))

from typing import ListNode
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    #두 리스트 병합
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 and l2:
            if l1.val > l2.val:
                l1,l2 = l2,l1
            l1.next = self.mergeTwoLists(l1.next,l2)
        return l1 or l2


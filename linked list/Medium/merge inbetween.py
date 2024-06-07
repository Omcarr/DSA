# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, l1: ListNode, a: int, b: int, l2: ListNode) -> ListNode:
        d1=l1
        for _ in range(a-1):
           d1=d1.next

        d2=d1.next
        for _ in range(b-a+1):
            d2=d2.next
        
        d1.next=l2
        while l2.next:
            l2=l2.next
        l2.next=d2

        return l1

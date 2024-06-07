# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        value = 0
        while head:
            value = value * 10 + head.val
            head = head.next

        value *= 2

        if value == 0:
            return ListNode(0)
        
        dummy = ListNode()
        current = dummy
        while value:
            digit = value % 10
            current.next = ListNode(digit)
            current = current.next
            value //= 10
        
        prev=None
        curr=dummy.next
        while curr:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
    
        return prev

              
        
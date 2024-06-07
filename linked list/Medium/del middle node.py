# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next == None:
            return None
        slow=head
        fast=head
        fast=fast.next.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        #middle reached for slow.next,so skip one
        slow.next=slow.next.next
        return head
            

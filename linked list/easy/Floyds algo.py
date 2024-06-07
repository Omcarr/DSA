# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


#tortoise hare algo
class Solution:
    def hasCycle(self, head) -> bool:
        turtle,hare=head,head

        while hare and hare.next:
            turtle=turtle.next
            hare=hare.next.next
            if turtle==hare:
             return True
             
        return False

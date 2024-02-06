# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head):
        curr,res=head,head
        cnt=0
        while curr:
            cnt+=1
            curr=curr.next
        
        mid=cnt//2

        while mid:
            res=res.next
            mid-=1
        return res

#optimal sol 
class Solution:
    def middleNode(self, head):
        slow = head
        fast = head
        while fast  and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
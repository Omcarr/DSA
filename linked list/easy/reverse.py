# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head
        # 1-->2-->3 then prev=none and curr=1 
        #we need curr=3 then the list is reversed
        while curr:
            temp = curr.next #next head value saved
            curr.next = prev #direction reversed as head would have gone to next we made it point to prev
            prev = curr #prev will hvae curr value
            curr = temp #new curr value have next head
            #and this will continue till curr value becones null as after the last node becomes a head no next node will exist and the lost would be reversed
        return prev

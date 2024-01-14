#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution():
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummynode=ListNode()
        tail=dummynode
        while l1 and l2:
         if l1.val<l2.val:
            tail.next=l1
            l1=l1.next
         else:
            tail.next=l2
            l2=l2.next
         tail=tail.next
         
        if l1:
         tail.next= l1
        else:
         tail.next=l2
        return dummynode.next
    
linkl=Solution()
l1 = ListNode(1, ListNode(3, ListNode(5)))
l2 = ListNode(2, ListNode(4, ListNode(6)))

A=linkl.mergeTwoLists(l1,l2)
while A:
    print(A.val, end="-->")
    A=A.next
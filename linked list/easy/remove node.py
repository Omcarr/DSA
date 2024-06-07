class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNode(head,n):
        #head = [1,2,3,4,5], n = 2
        dummy=ListNode(next=head)
        prev=dummy
        curr=head
        while n!=0:
            prev=curr.next
            curr=curr.next
            n-=1
        return prev.next

values=[1,2,3,4,5]
head = head = ListNode(values[0], ListNode(values[1], ListNode(values[2], ListNode(values[3], ListNode(values[4])))))
print(removeNode(head=head, n = 2))
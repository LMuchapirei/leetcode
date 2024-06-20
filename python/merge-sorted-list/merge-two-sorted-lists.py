# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1 # take the current node (l1) and put it into the tail
                l1 = l1.next   # take the next node in the first list and assign it to l1
            else:
                tail.next = l2 # take the current node (l2) and put it into the tail
                l2= l2.next    # take the next node in the first list and assign it to l2
            tail = tail.next   # move tail to the next one which is null since there is nothing
        
        if l1:
            tail.next = l1 # if the nodes are not of a similar size then copy the rest to the end of tail
        elif l2:
            tail.next = l2

        return dummy.next # dummy points to ListNode() first and the next node is what we want to return
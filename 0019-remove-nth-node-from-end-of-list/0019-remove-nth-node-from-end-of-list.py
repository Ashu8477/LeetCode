# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        slow=head
        fast=head

        for i in range(n):
            fast=fast.next
        
        prev=None
        while fast:
            prev=slow
            slow=slow.next
            fast=fast.next
        if prev is None:
            return head.next
        prev.next=slow.next
        return head
        
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow=head
        fast=head

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        prev=None
        while slow:
            next_node=slow.next
            slow.next=prev
            prev=slow
            slow=next_node

        right=prev
        left=head
        
        while right:
            if right.val != left.val:
                return False
            right=right.next
            left=left.next
        return True

        
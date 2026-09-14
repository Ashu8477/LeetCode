# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry=0
        valuee=0
        dummy=ListNode(0)
        head=dummy

        while l1 or l2 or carry:
            x=l1.val if l1 else 0
            y=l2.val if l2 else 0

            add=x+y+carry 
            carry=add//10
            digit=add%10
            dummy.next=ListNode(digit)
            dummy=dummy.next
            if l1:
                l1=l1.next
            if l2:
                l2=l2.next


        return head.next

        
            
        

        
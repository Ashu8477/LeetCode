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

        while l1 and l2:
            add=l1.val+l2.val+carry
            
            if add>9:
                carry=1
                add=add%10
            else:
                carry=0
            dummy.next=ListNode(add)
            dummy=dummy.next
            l1=l1.next
            l2=l2.next
        while l1:
            add=l1.val+carry
            
            if add>9:
                carry=1
                add=add%10
            else:
                carry=0
            dummy.next=ListNode(add)
            dummy=dummy.next
            l1=l1.next
        while l2:
            add=l2.val+carry
            
            if add>9:
                carry=1
                add=add%10
            else:
                carry=0
            dummy.next=ListNode(add)
            dummy=dummy.next
            l2=l2.next
        if carry==1:
            dummy.next=ListNode(carry) 

        return head.next

        
            
        

        
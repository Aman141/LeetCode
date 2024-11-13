# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 : return l2
        if not l2 : return l1
        else:
            carry = 0
            ans = ListNode(-1)
            prev = ans
            while (l1 or l2 or carry):
                x1 = l1.val if l1 else 0
                x2 = l2.val if l2 else 0
                x = (x1+x2+carry)%10
                carry = (x1+x2+carry)//10
                prev.next = ListNode(x)
                prev = prev.next
                if l1 : l1 = l1.next
                if l2 : l2 = l2.next
            
            return ans.next
        
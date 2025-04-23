# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head or not head.next: return head

        dummy = ListNode(-1)
        dummy.next= head
        first = dummy
  
        while first and first.next:
            second = first.next
            if second.val<x:
                first = first.next
                
            else:
                temp = second
                while(second.next and second.next.val>=x):
                    second = second.next

                if not second.next:
                    break
                first.next = second.next
                second.next = second.next.next
                first = first.next
                first.next = temp
            # printn(temp1)
        return dummy.next        

        
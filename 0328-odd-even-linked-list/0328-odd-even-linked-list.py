# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next or not head.next.next: return head

        odd = head
        first_even = head.next
        while odd.next:
            even = odd.next
            odd.next = even.next
            if not odd.next:
                break
        
            odd = odd.next
            even.next = odd.next

        odd.next = first_even

        return head    
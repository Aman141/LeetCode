# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next or not head.next.next: return head

        curr = head
        first_even = head.next
        while curr.next:
            temp_even = curr.next
            curr.next = curr.next.next
            if not curr.next:
                break
            temp_even.next = temp_even.next.next

            curr = curr.next

        curr.next = first_even

        return head    
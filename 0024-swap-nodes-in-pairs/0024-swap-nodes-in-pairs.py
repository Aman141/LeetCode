# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        def swapPair(first, second):
            first.next = second.next
            second.next = first

            return first,second

        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy
        first = head
        while first and first.next:
            second = first.next
            first,second = swapPair(first,second)
            prev.next = second
            prev = first

            first = prev.next


        return dummy.next   
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        ans = head.next        
        def swapPair(first, second):
            first.next = second.next
            second.next = first

            return first,second

        temp = ListNode(-1)
        first = head
        second = head.next
        while True:
            first,second = swapPair(first,second)
            temp.next = second
            temp = first
            if first.next and first.next.next:
                first = first.next
                second = first.next


            else:
                break    

            

        return ans   
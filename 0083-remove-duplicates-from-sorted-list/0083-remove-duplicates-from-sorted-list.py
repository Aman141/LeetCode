# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head : return None
        temp_1, temp_2 = head, head.next
        while(temp_2):
            if temp_1.val!=temp_2.val:
                temp_1.next = temp_2
                temp_1 = temp_2
            temp_2 = temp_2.next
        temp_1.next = None
        return head       


        
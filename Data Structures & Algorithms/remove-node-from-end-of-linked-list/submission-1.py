# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or (not head.next and n > 1):
            return None
        temp_head = head
        count = 1
        while temp_head.next:
            temp_head = temp_head.next
            count += 1
        index = count - n
        count = 0
        temp_head = head
        if index == 0:
            next_node = temp_head.next
            temp_head.next = None
            return next_node
        while temp_head.next and count < index - 1:
            count += 1
            temp_head = temp_head.next
        temp_head.next = (temp_head.next).next
        return head

        # technically O(n) time and O(1) space, but there is a better approach w fast/slow pointers

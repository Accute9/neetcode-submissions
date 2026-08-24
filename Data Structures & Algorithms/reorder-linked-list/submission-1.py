# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return None
        left = head
        temp_head = head
        mid = temp_head
        while temp_head and temp_head.next:
            temp_head = temp_head.next.next
            mid = mid.next
        temp_head = head
        while temp_head.next:
            temp_head = temp_head.next
        right = temp_head
        # left, mid, right setup, now reverse second-half
        prev = None
        temp_mid = mid
        while temp_mid:
            next_node = temp_mid.next
            temp_mid.next = prev
            prev = temp_mid
            temp_mid = next_node
        temp_left = left
        temp_mid = mid
        temp_right = right
        while temp_left and temp_left.next and temp_right and temp_right.next:
            next_right = temp_right.next
            next_left = temp_left.next
            temp_left.next = temp_right
            temp_right.next = next_left
            temp_right = next_right
            temp_left = next_left

# O(n) time, O(1) space


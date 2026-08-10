# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new_list = []
        head = None
        head_ref = None
        if not list1 and list2:
            return list2
        if not list2 and list1:
            return list1
        if not list1 and not list2:
            return None
        while list1 and list2:
            if list1.val <= list2.val:
                if head == None:
                    head = list1
                    head_ref = head
                else:
                    head.next = list1
                    head = head.next
                list1 = list1.next
                if not list1:
                    head.next = list2
                    return head_ref
            else:
                if head == None:
                    head = list2
                    head_ref = head
                else:
                    head.next = list2
                    head = head.next
                list2 = list2.next
                if not list2:
                    head.next = list1
                    return head_ref
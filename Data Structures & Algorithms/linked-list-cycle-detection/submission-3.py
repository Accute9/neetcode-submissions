class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        temp = head
        index = 0
        if not head or not head.next:
            return False
        while temp.next:
            seen.add(temp)
            if temp.next in seen:
                return True
            temp = temp.next
        return False
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        temp = head
        count = 0
        if not head or not head.next:
            return False
        while temp.next:
            index = temp.val
            if index < count:
                return True
            temp = temp.next
            count += 1
        return False

# optimal time/space, O(1) space by using counter instead of set
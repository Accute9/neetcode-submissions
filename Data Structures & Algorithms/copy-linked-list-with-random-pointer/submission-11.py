"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        nodes = {}
        temp_head = head
        while temp_head:
            new_node = Node(temp_head.val)
            nodes[temp_head] = new_node
            temp_head = temp_head.next
        temp_head = head
        while temp_head:
            if temp_head.next:
                nodes[temp_head].next = nodes[temp_head.next]
            else:
                nodes[temp_head].next = None
            if temp_head.random:
                nodes[temp_head].random = nodes[temp_head.random]
            else:
                nodes[temp_head].random = None
            temp_head = temp_head.next
        return nodes[head]

# O(n) time, O(n) space
             
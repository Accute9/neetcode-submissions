# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def check_balance(left_height, right_height):
            if abs(left_height - right_height) <= 1:
                return True
            return False
        def dfs(root):
            if not root:
                return 0
            left = 1 + dfs(root.left)
            if left == 0:
                return -1
            right = 1 + dfs(root.right)
            if right == 0:
                return -1
            if not check_balance(left, right):
                return -1
            height = max(left, right)
            return height
        if dfs(root) == -1:
            return False
        left_height = dfs(root.left)
        right_height = dfs(root.right)
        return abs(left_height - right_height) <= 1
    
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def func(node):
            if not node:
                return 0
            
            l = float("inf")
            r = float('inf')

            if node.left:
                l = func(node.left)
            if node.right:
                r = func(node.right)
            
            return 1 + min(l, r) if not (1 + min(l, r) == float("inf")) else 1

        return func(root)
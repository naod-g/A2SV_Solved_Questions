# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.res = 0

        def dfs(node, path):
            if not node: return
            path += node.val

            if path == targetSum:
                self.res += 1
            dfs(node.left, path)
            dfs(node.right, path)

        def traverse(node):
            if not node: return

            dfs(node, 0)
            if node.left: traverse(node.left)
            if node.right: traverse(node.right)
            
        traverse(root)
        return self.res
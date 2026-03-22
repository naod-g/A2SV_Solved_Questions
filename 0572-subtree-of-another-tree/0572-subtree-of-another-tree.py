# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def compare(s, t):
            if not(s and t):
                return s is t

            if s.val == t.val:
                if compare(s.left, t.left) and compare(s.right, t.right):
                    return True
            return False
        
        if compare(root, subRoot): return True
        if not root: return False
        return (self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot))

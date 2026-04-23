# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        visited = set()
        q = deque()
        q.append(root)

        while q:
            node = q.popleft() 
            visited.add(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)


        return len(visited) == 1

        
